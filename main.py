from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars_and_counts
import sys
import requests
import os
from os import system

"""
Still want to work on: 
    make option to output the report to terminal if wanted
    add error handling
    add different analysis features
"""

def get_book_text(path_to_file):
    with open(path_to_file) as f: #with block opens a file
        file_contents = f.read() #.read() method puts content into a string
    return file_contents

def main():  
    
    welcome()

    dir_setup()

    first_loop = True
    while ask_run_analyzer(first_loop) == 'yes': # main book loop

        book_type = get_book_type()    

        if book_type == "local":
            generate_report(get_book_local_path())
            #display_report(get_book_local_path()) # display the contents of the report to the terminal
        elif book_type == "online":
            generate_report(url_to_txt_file(get_book_url(), get_new_txt_file_name()))
            #display_report(url_to_txt_file(get_book_url(), get_new_txt_file_name())) # display the contents of the report to the terminal
        else: 
            pass # block reserved in case other methods of getting books are ever added
        first_loop = False 

    end()

def dir_setup():
    print("Checking if /books and /reports directories exist...")

    if os.path.isdir('books'):
        print("Found existing /books directory.")
    else:
        print("/books directory not found, creating one...")
        os.mkdir('books')
        print("/books directory succesfully created!")

    if os.path.isdir('reports'):
        print("Found existing /reports directory.")
    else:
        print("/reports directory not found, creating one...")
        os.mkdir('reports')
        print("/reports directory succesfully created!")
    

def welcome():
    print("Welcome to BookBot, by @jeffschoe")
    print("BookBot will analyze a book for you, either saved locally or pulled from the web!\n")
    return

def ask_run_analyzer(first_loop):

    if first_loop == True:
        print("\nLet's anaylze your first book!\n")
        print(f"Ready to get started? Type \"yes\" or \"no\".\n")
        answer_run_analyzer = input("Response: ")
        print("")
        return answer_run_analyzer
    else:
        print(f"Would you like to analyze another book? Type \"yes\" or \"no\".\n")
        answer_run_analyzer = input("Response: ")
        print("")
        return answer_run_analyzer

def get_book_type(): # get the type of book user wants to analyze
    print("If you would like to analyze a local book, type \"local\". "
    "If you would like to analyze an online book, type \"online\".\n")
    book_type = input("Response: ")
    print("")
    return book_type

def get_book_local_path(): # gets the local patch to the book
    book_local_path = input("Input the path to your locally saved book: ")
    return book_local_path

def url_to_txt_file(book_url, new_book_txt_name): 
    response = requests.get(book_url) # get the book from the web
    with open(f'books/{new_book_txt_name}', 'wb') as f:
        f.write(response.content) # writes book to file
    return f'books/{new_book_txt_name}'

def get_book_url(): # gets the url to the book from the user
    book_url = input("Input the url to the book: ")
    print("")
    return book_url

def get_new_txt_file_name(): # asks user to specify the new file name for their book
    new_txt_name = input("Input a new file name, such as \"example.txt\", to write the book to: ")
    print("")
    return new_txt_name

def generate_report(path_to_book_file): # creates the report
    book_file_name = f"{path_to_book_file.split('/')[-1]}" # pull file name out of path
    book_name = f"{book_file_name.split('.')[0]}" # pull book name out of file name
    try:
        with open(f"reports/{book_name}_report.txt", "x") as f:
            f.write("\n========= BOOKBOT REPORT =========")
            f.write(f"\nAnalyzing book found at {path_to_book_file}")

            f.write("\n\n----------- Word Count ----------")
            f.write(f"\nFound {get_num_words(get_book_text(path_to_book_file))} total words")
            
            f.write("\n\n--------- Character Count -------")
            count_of_chars = get_num_chars(get_book_text(path_to_book_file))
            sorted_chars_and_counts = sort_chars_and_counts(count_of_chars) #list of dictionaries

            i = 0
            while i < len(sorted_chars_and_counts):
                if sorted_chars_and_counts[i]["character"].isalpha():
                    f.write(f"\n{sorted_chars_and_counts[i]["character"]}: {sorted_chars_and_counts[i]["count"]}")
                    i +=1
                else:
                    i += 1

            f.write("\n\n============= END ===============\n")
    except FileExistsError:
        print(f"\nFilename \"{book_name}_report.txt\" already exists, new file not created.")

    return

def display_report(path_to_book_file): # prints the report ***this will eventually just cat the report out to terminal

    print("\n========= BOOKBOT REPORT =========")
    print(f"Analyzing book found at {path_to_book_file}")

    print("\n----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(path_to_book_file))} total words")
    
    print("\n--------- Character Count -------")
    count_of_chars = get_num_chars(get_book_text(path_to_book_file))
    sorted_chars_and_counts = sort_chars_and_counts(count_of_chars) #list of dictionaries

    i = 0
    while i < len(sorted_chars_and_counts):
        if sorted_chars_and_counts[i]["character"].isalpha():
            print(f"{sorted_chars_and_counts[i]["character"]}: {sorted_chars_and_counts[i]["count"]}")
            i +=1
        else:
            i += 1

    print("\n============= END ===============\n")
    return

'''
def display_report(path): # path to the .txt file
    system(f"cat {path}")# so it can cat it out to the terminal
'''

def end():
    print("Thank you for using BookBot!\n")
    sys.exit(1) # close program

main()




























































