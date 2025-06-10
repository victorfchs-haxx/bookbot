def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    print(f"Found {word_count} total words")

def count_characters(text):
    str_text = str(text).lower()
    char_counts = {}
    for char in str_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def convert_list(char_counts):
    my_list = list(char_counts.items())
    format_list = []
    for char, num in my_list:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = num
        format_list.append(new_dict)
    key = lambda indiv_dict: indiv_dict["num"]
    format_list.sort(reverse=True, key=key)
    return format_list
