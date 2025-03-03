def get_book_text(path_to_file):
    with open(path_to_file) as f: #with block opens a file
        file_contents = f.read() #.read() method puts content into a string
    return file_contents

def main():
    print(f"{get_book_text("./books/frankenstein.txt")}")
    return

main()




























































