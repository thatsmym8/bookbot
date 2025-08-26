import sys

from stats import newdict
from stats import print_word_count

def char_count_print(file_path):
    for i in newdict(file_path):
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

def main(file_path):
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {f"{file_path}"}...")
    print("----------- Word Count ----------")
    print_word_count(file_path)
    print("--------- Character Count -------")
    char_count_print(file_path)
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
      
main(sys.argv[1])