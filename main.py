from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars_and_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f: #with block opens a file
        file_contents = f.read() #.read() method puts content into a string
    return file_contents

def main():  
    welcome()

    if get_book_type() == "local":
        generate_report(get_book_path())
    elif get_book_type == "online":
        pass
    else:
        pass

    """
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    """

def welcome(): # introduce the program
    print("Welcome to Bookbot, by @jeffschoe")
    print("You will be able to get an analysis on a book either saved locally or from the web.\n")
    return

def get_book_type(): # get the type of book user wants to analyze
    print("If you would like to analyze a local book, type \"local\". If you would like to analyze an online book, type \"online\".\n")
    book_type = input("")
    print("")
    return book_type

def get_book_path(): # gets the local patch to the book
    book_path = input("Input the path to your locally saved book: ")
    return book_path

def get_book_url(): # gets the url to the book from the user
    pass
                
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

    print("============= END ===============")

    return


main()




























































