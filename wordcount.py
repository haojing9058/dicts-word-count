# put your code here.
# read and load file


def word_counter(filename):
    """"""

    text_file = open(filename)
    # text_file = open("twain.txt")
    # index by the spaces between words
    # list_of_words = []

    my_dict = {}

    for line in text_file:
        line = line.rstrip()
        words = line.split(" ")
        # list_of_words.extend(words)
        for word in words:
            my_dict[word] = my_dict.get(word, 0) + 1

    # print list_of_word
    # print my_dict.items()

    for word, count in my_dict.items():
        print "{} {}".format(word, count)

# for word in words:


# think about how to handle \n later

# iterate through text file
    # if word is new, add to dictionary
    # if word is already added to dict, increment by 1
# return key (word) and value (how many times word shows up)

word_counter("test.txt")
