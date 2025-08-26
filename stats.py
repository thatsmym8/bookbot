
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read().lower()
    return file_contents

def count_words(file_path):
    return len(get_book_text(file_path).split())

def print_word_count(file_path):
    return print(f"Found {count_words(file_path)} total words")

def count_characters(file_path):
    characters = {}
    for c in get_book_text(file_path):
        if c not in characters:
            characters[c] = 0
        characters[c] += 1
    return characters

def sort_on(items):
    return items["num"]


def newdict(file_path):
    char_counts = count_characters(file_path)
    new_list = [{"char":k, "num":v} for k, v in char_counts.items()]
    new_list.sort(reverse=True, key=sort_on)
    return new_list