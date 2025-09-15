from stats import number_of_words
from stats import count_characters
from stats import sort_characters
from stats import sort_on

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(book_text)
    char_count = count_characters(book_text)
    sorted_char_count = sort_characters(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
main()