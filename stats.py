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