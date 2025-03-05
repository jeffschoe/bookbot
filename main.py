from stats import get_num_words
from stats import get_num_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f: #with block opens a file
        file_contents = f.read() #.read() method puts content into a string
    return file_contents

def main():
    #print(f"{get_book_text("./books/frankenstein.txt")}")
    print(f"{get_num_words(get_book_text("./books/frankenstein.txt"))} words found in the document")
    count_of_chars = get_num_chars(get_book_text("./books/frankenstein.txt"))
    print(count_of_chars)
    
    return

main()




























































