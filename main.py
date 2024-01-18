import string

PATH_TO_FILE = "books/Frankenstein.txt"

def main():
    content = get_file_contents(PATH_TO_FILE)
    report(content)

def report(content):
    print(f"--- Begin report of {PATH_TO_FILE} ---")
    print(f"{get_word_count(content)} words found in the document")
    print_all_element_count(get_char_count(content))
    print("--- End report ---")

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
    # print(f"letter {letters}")
    for c in letters:
        dict[c] = 0
    
    for c in words:
        c_lower = c.lower()
        if c_lower in dict.keys():
            dict[c_lower] += 1
    
    return dict

def print_all_element_count(char_dict):
    list = []
    for key, value in char_dict.items():
        list.append((key, value))
    list.sort(key=lambda a: a[1])

    # print(f"list count {len(list)}")
    
    # reverse index and print all values
    for idx in range(len(list)-1,-1,-1):
        item = list[idx]
        print(f"The '{item[0]}' character was found {item[1]} times")

main()