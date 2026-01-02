from stats import word_count, letter_count, sorted_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as input:
        return input.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    book = get_book_text(sys.argv[1])
    print(f'Found {word_count(book)} total words')
    print("--------- Character Count -------")
    sorted_charas = sorted_dicts(letter_count(book))
    for chara in sorted_charas:
        if chara["char"].isalpha():
            print(f"{chara["char"]}: {chara["num"]}")

main()