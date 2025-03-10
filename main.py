import sys

from stats import number_of_words
from stats import number_of_characters
from stats import sorted_dictionary

def get_book_text(bookpath):
    with open(bookpath) as f:
        file_contents=f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = number_of_words(book)
    print(f"Found {word_count} total words")
    char_count = number_of_characters(book)
    # print(char_count)
    sorted_dic = sorted_dictionary(char_count)
    for entry in sorted_dic:
        print(f"{entry["character"]}: {entry["count"]}")

main()