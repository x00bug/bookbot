import sys
from stats import get_word_count, get_char_count, get_book_text, get_sorted_chars
def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    # Declare book path variable to be the input
    book_path = sys.argv[1]

    # Load the book text
    book_text = get_book_text(book_path)
    
    # Get stats
    words = get_word_count(book_text)
    sorted_chars = get_sorted_chars(get_char_count(book_text))

    # Output Results
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


main()
