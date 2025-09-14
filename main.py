from stats import number_of_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(book_text)
    char_count = count_characters(book_text)
    print(f"{num_words} words found in the document")
    print(char_count)


main()