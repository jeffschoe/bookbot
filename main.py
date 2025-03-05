from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars_and_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f: #with block opens a file
        file_contents = f.read() #.read() method puts content into a string
    return file_contents

def main():
    #print(f"{get_book_text("./books/frankenstein.txt")}")
    print("============ BOOKBOT ============")
    print("Analyzing book found at TBD")

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text("./books/frankenstein.txt"))} total words")
    
    print("--------- Character Count -------")
    count_of_chars = get_num_chars(get_book_text("./books/frankenstein.txt"))
    #print(count_of_chars) prints unsorted dictionary
    sorted_chars_and_counts = sort_chars_and_counts(count_of_chars) #list of dictionaries
    #print(sorted_chars_and_counts) prints sorted list of dictionaries
    i = 0
    while i < len(sorted_chars_and_counts):
        if sorted_chars_and_counts[i]["character"].isalpha():
            #print(sorted_chars_and_counts[i])
            print(f"{sorted_chars_and_counts[i]["character"]}: {sorted_chars_and_counts[i]["count"]}")
            i +=1
        else:
            i += 1

    print("============= END ===============")

    return

main()




























































