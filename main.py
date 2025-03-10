def get_book_text(bookpath):
    with open(bookpath) as f:
        file_contents=f.read()
    return file_contents

def number_of_words(book):
    words = book.split()
    counter = 0
    for word in words:
        counter +=1
    return counter

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = number_of_words(book)
    print(f"{word_count} words found in the document")


main()