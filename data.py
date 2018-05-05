""" Sets up the data for the neural network """
import pandas as pd  # Provides data structures and data analysis
import tensorflow as tf  # Provides the basis for neural networks
import sys
import csv

# Dirty solution to the data set being too large for pandas
maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

TRAIN_PATH = "data/collated_train"
TEST_PATH = "data/collated_test"
CSV_COLUMN_NAMES = ['Char1', 'Char2', 'Char3', 'Char4', 'Char5', 'Char6', 'Char7',
                    'Char8', 'Char9', 'Char10', 'Char11', 'Char12', 'Char13', 'Char14',
                    'Char15', 'Char16', 'Language']
CSV_TYPES = [[''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], ['']]
LANGUAGE = ['English', 'Spanish', 'Italian', 'German']


# Note to self:
# y means label
# x means feature
def load_data(y_name='Language'):
    """ Reads in the csv file for testing and training """
    train = pd.read_csv(TRAIN_PATH, names=CSV_COLUMN_NAMES, header=0, engine='python')
    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(TEST_PATH, names=CSV_COLUMN_NAMES, header=0, engine='python')
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)


def train_input_fn(features, labels, batch_size=100):
    """ Used for training from the inputs """
    train_dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    train_dataset = train_dataset.shuffle(500000).repeat().batch(batch_size)

    return train_dataset


def test_input_fn(features, labels, batch_size=100):
    """ Used for evaluating from the inputs """
    features = dict(features)
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)

    test_dataset = tf.data.Dataset.from_tensor_slices(inputs)
    assert batch_size is not None, "batch_size must not be none"
    test_dataset = test_dataset.batch(batch_size)

    return test_dataset


def parse_line(line):
    fields = tf.decode_csv(line, record_defaults=CSV_TYPES)
    features = dict(zip(CSV_COLUMN_NAMES, fields))
    label = features.pop('Language')

    return features, label


def csv_input(csv_path, batch_size):
    dataset = tf.data.TextLineDataset(csv_path).skip(1)
    dataset = dataset.map(parse_line)
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    return dataset


def main(argv):
    print(load_data())


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
