def get_book_text(path_to_file):
    with open(path_to_file) as f: #with block opens a file
        file_contents = f.read() #.read() method puts content into a string
    return file_contents

def num_words(book_text):
    return len(book_text.split())

def main():
    #print(f"{get_book_text("./books/frankenstein.txt")}")
    print(f"{num_words(get_book_text("./books/frankenstein.txt"))} words found in the document")
    return

main()




























































