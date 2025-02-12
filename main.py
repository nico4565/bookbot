def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dict = get_num_characters(text)
    list_of_dict = get_list_only_char_dict(characters_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    list_of_dict.sort(reverse=True, key=sort_on)
    for dict in list_of_dict:
        for k in dict:
            print(f"The '{k}' character was found {dict[k]} times")
    
    print(f"--- End report of {book_path} ---")


def sort_on(dict):
    return list(dict.values())[0]

def get_list_only_char_dict(dict):
    list_of_dict = []
    for k in dict:
        if k.isalpha():
            list_of_dict.append({k:dict[k]})
    return list_of_dict

def get_num_characters(text):
    characters_counter_dict = {}
    lower_case_text = text.lower()
    for ch in lower_case_text:
        if ch in characters_counter_dict:
            characters_counter_dict[ch] += 1
        else:
            characters_counter_dict[ch] = 1

    return characters_counter_dict

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()