def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def get_word_count(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    char_count_dict = {}
    for char in book_text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def get_sorted_chars(char_count_dict):
    def sort_on(single_dict):
        return single_dict["num"]

    list_of_dicts = [
        {"char": key, "num": value}
        for key, value in char_count_dict.items()
    ]

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
