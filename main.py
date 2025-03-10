import sys

from stats import number_of_words
from stats import number_of_characters
from stats import sorted_dictionary

def get_book_text(bookpath):
    with open(bookpath) as f:
        file_contents=f.read()
    return file_contents

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        file_path = sys.argv[1]
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        book = get_book_text(file_path)
        word_count = number_of_words(book)
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        char_count = number_of_characters(book)
        sorted_dic = sorted_dictionary(char_count)
        for entry in sorted_dic:
            print(f"{entry["character"]}: {entry["count"]}")
        print("============= END ===============")

main()