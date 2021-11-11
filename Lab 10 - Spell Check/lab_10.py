import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

def main():

    dictionary = open("dictionary.txt")
    dictionary_list = []

    for line in dictionary:
        line = line.strip()

        dictionary_list.append(line)
    dictionary.close()
    print("---Linear Search---")
    alice_story = open("AliceInWonderLand200.txt")
    line_numb = 0
    for line in alice_story:
        word_list = split_line(line)
        line_numb += 1
        for word in word_list:
            key = word.upper()
            current_list_position = 0
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != key:
                current_list_position += 1
            if current_list_position == len(dictionary_list):
                print("line", line_numb,"possible misspelled word", word)

    alice_story.close()

    print("---Binary Search---")

    dictionary = open("dictionary.txt")
    dictionary_list = []

    for line in dictionary:
        line = line.strip()

        dictionary_list.append(line)
    dictionary.close()
    alice_story = open("AliceInWonderLand200.txt")
    line_numb = 0
    for line in alice_story:
        word_list = split_line(line)
        line_numb += 1
        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list)
            found = False

            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                elif dictionary_list != key:
                    found = True
            if not found:
                print("line", line_numb, "possible misspelled word", word)









main()






