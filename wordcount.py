# put your code here.
# read and load file
from sys import argv
# print(sys.argv, len(sys.argv))
# "wordcount.py" = sys.argv[0]
# "test.txt" = sys.argv[1:]


def word_counter(filename):
    """Takes a text file and returns how many times a word shows up!"""

    text_file = open(filename)
    # text_file = open("twain.txt")
    # index by the spaces between words
    # list_of_words = []

    my_dict = {}

    for line in text_file:
        line = line.replace(",", "").replace("!", "").replace("?", "").replace(".", "")
        # the above works but is so ugly
        line = line.rstrip()
        words = line.split(" ")
        # list_of_words.extend(words)
        for word in words:
            word = word.lower()
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

word_counter(argv[1])
