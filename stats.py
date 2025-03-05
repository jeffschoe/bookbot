def get_num_words(book_text):
    return len(book_text.split())

def get_num_chars(book_text):
    lower_book_text = book_text.lower()
    total_chars_and_counts = {}
    for char in lower_book_text:
        if char in total_chars_and_counts:
            total_chars_and_counts[char] += 1
        else: 
            total_chars_and_counts[char] = 1
    return total_chars_and_counts

def sort_on(dict):
    return dict["count"]

def sort_chars_and_counts(chars_and_counts_dict):
    unsorted_dicts_list = []
    sorted_dicts_list = []
    for char_and_count in chars_and_counts_dict:
        temp_dict = {"character": char_and_count, "count": chars_and_counts_dict[char_and_count]}
        unsorted_dicts_list.append(temp_dict)
        #now have list of dicts, but need to sort it
        unsorted_dicts_list.sort(reverse=True, key=sort_on)
        sorted_dicts_list = unsorted_dicts_list
        #sort_on part is not working yet.
    return sorted_dicts_list