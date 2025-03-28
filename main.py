from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars_and_counts
import sys
import requests

"""
Still want to work on: 
    distinguish between first use and continued uses within the loop
    add way to automatically save reports to a file called reports.
    add error handling
"""

def get_book_text(path_to_file):
    with open(path_to_file) as f: #with block opens a file
        file_contents = f.read() #.read() method puts content into a string
    return file_contents

def main():  

    welcome()

    first_loop = True

    while ask_run_analyzer(first_loop) == 'yes': # main book loop

        book_type = get_book_type()    

        if book_type == "local":
            generate_report(get_book_local_path())
        elif book_type == "online":
            generate_report(url_to_txt(get_book_url(), get_new_txt_name()))
        else: 
            pass # block reserved in case other methods of getting books are ever added
        
        first_loop = False 

    end()

def welcome(): # introduce the program
    print("Welcome to Bookbot, by @jeffschoe")
    print("Bookbot will analyze a book for you, either saved locally or pulled from the web!\n")
    return

def ask_run_analyzer(first_loop):

    if first_loop == True:
        print("Let's anaylze your first book!\n")
        print(f"Would you like to continue? Type \"yes\" or \"no\".\n")
        answer_run_analyzer = input("Response: ")
        print("")
        return answer_run_analyzer
    else:
        print(f"Would you like to analyze another book? Type \"yes\" or \"no\".\n")
        answer_run_analyzer = input("Response: ")
        print("")
        return answer_run_analyzer

def get_book_type(): # get the type of book user wants to analyze
    print("If you would like to analyze a local book, type \"local\". If you would like to analyze an online book, type \"online\".\n")
    book_type = input("Response: ")
    print("")
    return book_type

def get_book_local_path(): # gets the local patch to the book
    book_local_path = input("Input the path to your locally saved book: ")
    return book_local_path

def get_book_url(): # gets the url to the book from the user
    book_url = input("Input the url to the book: ")
    print("")
    return book_url

def get_new_txt_name(): # asks user to specify the new file name for their book
    new_txt_name = input("Input a new file name, such as \"example.txt\", to write the book to: ")
    print("")
    return new_txt_name

def url_to_txt(book_url, new_book_txt_name): 
    response = requests.get(book_url) # get the book from the web
    with open(f'books/{new_book_txt_name}', 'wb') as f:
        f.write(response.content) # writes book to file
    new_path_from_url = f'books/{new_book_txt_name}'
    return new_path_from_url

def make_path():
    pass # may break out function that take the new file and return a path to it, from right above in url_to_txt function

def generate_report(path_to_book_file): # prints the report

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book_file}")

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(path_to_book_file))} total words")
    
    print("--------- Character Count -------")
    count_of_chars = get_num_chars(get_book_text(path_to_book_file))
    sorted_chars_and_counts = sort_chars_and_counts(count_of_chars) #list of dictionaries

    i = 0
    while i < len(sorted_chars_and_counts):
        if sorted_chars_and_counts[i]["character"].isalpha():
            print(f"{sorted_chars_and_counts[i]["character"]}: {sorted_chars_and_counts[i]["count"]}")
            i +=1
        else:
            i += 1

    print("============= END ===============\n")
    return



def end():
    print("Thank you for using Bookbot!\n")
    sys.exit(1) # close program

main()




























































