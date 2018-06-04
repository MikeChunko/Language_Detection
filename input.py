""" Used for taking custom input to the neural network """


def read_word():
    """ Method for reading in the word """
    word = str()

    while True:
        word = input("Input the word to be tested or \'-1\' to quit: \n")
        if (word.isalpha() and word.__len__() <= 16) or word == "-1":
            break
        else:
            print("The word must contain only alphabetical characters and be a maximum of 16 characters long")

    sentinel = False

    if word == "-1":
        sentinel = True

    word = word.lower()

    return word, sentinel


def string_to_integer(word):
    """ Converts a string into the integer format expected by the neural network """
    integer_list = list()

    for character in word:
        integer_list.append(character)

    for index in range(integer_list.__len__()):
        current_character = integer_list[index]
        integer_list[index] = ord(current_character)

    for index in range(integer_list.__len__()):
        current_character = integer_list[index]
        integer_list[index] = current_character - ord('`')

    while integer_list.__len__() < 16:
        integer_list.append(0)

    return integer_list


def list_to_features(integer_list=[0] * 16):
    """ Converts the list provided by string_to_integer into a the feature lists """
    char1 = [integer_list[0]]
    char2 = [integer_list[1]]
    char3 = [integer_list[2]]
    char4 = [integer_list[3]]
    char5 = [integer_list[4]]
    char6 = [integer_list[5]]
    char7 = [integer_list[6]]
    char8 = [integer_list[7]]
    char9 = [integer_list[8]]
    char10 = [integer_list[9]]
    char11 = [integer_list[10]]
    char12 = [integer_list[11]]
    char13 = [integer_list[12]]
    char14 = [integer_list[13]]
    char15 = [integer_list[14]]
    char16 = [integer_list[15]]

    return char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, \
           char14, char15, char16


def input_features():
    """ Used for entering custom words to use for prediction """
    word = str()
    sentinel = False
    word, sentinel = read_word()

    integer_list = list()
    integer_list = string_to_integer(word)

    char1 = list()
    char2 = list()
    char3 = list()
    char4 = list()
    char5 = list()
    char6 = list()
    char7 = list()
    char8 = list()
    char9 = list()
    char10 = list()
    char11 = list()
    char12 = list()
    char13 = list()
    char14 = list()
    char15 = list()
    char16 = list()

    char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, \
    char14, char15, char16 = list_to_features(integer_list)

    return char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, char14, \
           char15, char16, sentinel


def main():
    while True:
        char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, char14, \
        char15, char16, sentinel = input_features()

        print(char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, char14,
              char15, char16, sentinel)

        if sentinel:
            break
        else:
            print("\n")


if __name__ == '__main__':
    main()
