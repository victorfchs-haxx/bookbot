from stats import count_words
from stats import count_characters
from stats import convert_list
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    count_words(text)
    print("--------- Character Count -------")
    char_counts = count_characters(text)
    format_list = convert_list(char_counts)
    for dict in format_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
