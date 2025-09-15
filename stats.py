def number_of_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(count_dict):
    return count_dict["num"]

def sort_characters(char_dict):
    char_list =[]
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list
