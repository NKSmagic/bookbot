def number_of_words(book):
    words = book.split()
    counter = 0
    for word in words:
        counter +=1
    return counter

def number_of_characters(book):
    char_counts = {}
    content = book.lower()

    for char in content:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

def sort_on(char_counts):
    return char_counts["count"]

def sorted_dictionary(char_count):
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"character": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list