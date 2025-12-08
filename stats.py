def count_words(text):
    return len(text.split())

def get_chars_count(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(item):
    return item["num"]

def sort_chars_count(char_dict):
    chars_count_list = []
    for c in char_dict:
        chars_count_list.append({ "char": c, "num": char_dict[c] })
    chars_count_list.sort(reverse=True, key=sort_on)
    return chars_count_list
