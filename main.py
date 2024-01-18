import string

PATH_TO_FILE = "books/Frankenstein.txt"

def main():
    content = get_file_contents(PATH_TO_FILE)
    print(content)
    print(f"get words count: {get_word_count(content)}")
    print(f"get char count: {get_char_count(content)}")

def get_file_contents(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(words):
    words = words.split()
    return len(words)

def get_char_count(words):
    dict = {}
    letters = set(string.ascii_lowercase)
    print(f"letter {letters}")
    for c in letters:
        dict[c] = 0
    
    for c in words:
        c_lower = c.lower()
        if c_lower in dict.keys():
            dict[c_lower] += 1
    
    return dict

main()