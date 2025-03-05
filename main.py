from stats import sort_on_count
from stats import get_num_words
import sys



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    print(f"{num_words} words found in the document")
    print(char_count)
    sorted_characters = sort_on_count(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...") 
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words") 

    # Character count section
    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["character"].isalpha():  # Skip non-alphabet characters
            print(f"{item['character']}: {item['count']}")
    
    # Footer
    print("============= END ===============")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    char_count ={}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
    

main()
