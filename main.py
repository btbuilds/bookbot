from stats import count_words_in_text, count_characters, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def get_booktext(filepath):
    booktext = ""
    with open(filepath) as f:
        booktext = f.read()
    return booktext

book_text = get_booktext(path_to_book)
num_words = count_words_in_text(book_text)
counted_characters = count_characters(book_text)
list_sorted_dicts = sort_dict(counted_characters)

def print_header():    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def print_chars(list_of_dict):
    print("--------- Character Count -------")
    for dict in list_of_dict:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

def print_report():
    print_header()
    print_chars(list_sorted_dicts)
    

def main():
    print_report()

main()