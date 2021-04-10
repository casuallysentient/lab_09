from pprint import pprint  # All this function does is print dictionaries nicely. You don't have to use it.


def get_word_counts(filepath):
    """
    Returns a dictionary containing the work frequencies of a corpus contained in a file pointed to by filepath.

    :param filepath: A string containing the location of a file.
    :return: A dictionary of word frequencies.
    """
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        return {}
    else:
        lists = [line.strip() for line in file]
        word_count = {}
        for x in lists:
            words = x.lower().split()
            for y in words:
                if y in word_count:
                    word_count[y] += 1
                else:
                    word_count[y] = 1
        return word_count




def main():
    """
    Some sample behavior based on the README.
    """
    sample_file_name = "lyrics.txt"
    word_freqs = get_word_counts(sample_file_name)
    pprint(word_freqs)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
