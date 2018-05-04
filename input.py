""" Used for taking custom input to the neural network """


def read_input():
    """ Simple method for reading in the word """
    word = str()

    while True:
        word = input("Input the word to be tested or \'-1\' to quit: \n")
        if word.isalpha() or word == "-1":
            break
        else:
            print("The word must contain only alphabetical characters")

    sentinel = False

    if word == "-1":
        sentinel = True

    return word, sentinel


def string_to_integer(word):
    """ Converts a string into the integer format expected by the neural network """
    integer_list = list()

    for character in word:
        integer_list.append(character)

    for index in range(integer_list.__len__()):
        current_character = integer_list[index]
        integer_list[index] = ord(current_character)

    return integer_list


def main():
    word, sentinel = read_input()
    print("\n", word, sentinel)

    list = string_to_integer(word)
    print("\n", list)


if __name__ == '__main__':
    main()
