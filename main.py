def main():
    book_path = "books/frankinstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    characters = get_character_count(text)
    char_dict = alpha_chars(characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()

    for item in char_dict:
        print(f"The '{item['letter']} character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lower_case = text.lower()
    characters = {}
    for char in lower_case:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_on(d):
    return d["num"]

def alpha_chars(dict):
    list_of_chars = []
    for k in dict:
        if k.isalpha():
            list_of_chars.append({"letter": k, "num": dict[k]})
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars




main()
