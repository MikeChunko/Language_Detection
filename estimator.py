""" The estimator for the neural network """
from __future__ import absolute_import
from __future__ import division

import tensorflow as tf
import data


def main(argv):
    with tf.Session() as session:
        (train_x, train_y), (test_x, test_y) = data.load_data()

        my_categorical_columns = [
            tf.feature_column.categorical_column_with_identity(key='Char1', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char2', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char3', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char4', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char5', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char6', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char7', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char8', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char9', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char10', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char11', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char12', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char13', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char14', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char15', num_buckets=27),
            tf.feature_column.categorical_column_with_identity(key='Char16', num_buckets=27),
        ]

        my_feature_columns = [
            tf.feature_column.indicator_column(my_categorical_columns[0]),
            tf.feature_column.indicator_column(my_categorical_columns[1]),
            tf.feature_column.indicator_column(my_categorical_columns[2]),
            tf.feature_column.indicator_column(my_categorical_columns[3]),
            tf.feature_column.indicator_column(my_categorical_columns[4]),
            tf.feature_column.indicator_column(my_categorical_columns[5]),
            tf.feature_column.indicator_column(my_categorical_columns[6]),
            tf.feature_column.indicator_column(my_categorical_columns[7]),
            tf.feature_column.indicator_column(my_categorical_columns[8]),
            tf.feature_column.indicator_column(my_categorical_columns[9]),
            tf.feature_column.indicator_column(my_categorical_columns[10]),
            tf.feature_column.indicator_column(my_categorical_columns[11]),
            tf.feature_column.indicator_column(my_categorical_columns[12]),
            tf.feature_column.indicator_column(my_categorical_columns[13]),
            tf.feature_column.indicator_column(my_categorical_columns[14]),
            tf.feature_column.indicator_column(my_categorical_columns[15]),
        ]

        # Changes the configuration for making checkpoints
        checkpoint_config = tf.estimator.RunConfig(
            save_checkpoints_secs=60, keep_checkpoint_max=2
        )
        # Creates a classifier with 4 hidden layers that can choose between 4 categories
        classifier = tf.estimator.DNNClassifier(
            feature_columns=my_feature_columns,
            hidden_units=[
                16, 15, 14, 13
            ],
            n_classes=4, model_dir='language_detector', config=checkpoint_config
        )

        batch_size = 1000
        train_steps = 5000

        # Uses the classifier to train the neural network
        classifier.train(
            input_fn=lambda: data.train_input_fn(train_x, train_y, batch_size),
            steps=train_steps
        )

        # Prints the accuracy of the trained model based on the test data
        eval_result = classifier.evaluate(
            input_fn=lambda: data.test_input_fn(test_x, test_y, batch_size)
        )

        print("Saved model to {}".format({classifier.model_dir}))

        # Highest: 87.65
        print("\nAccuracy with test data: {accuracy:0.3%}\n".format(**eval_result))


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
