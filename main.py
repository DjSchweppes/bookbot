def main():
    book_path = "books/frankinstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    characters = get_character_count(text)
    char_dict = alpha_chars(characters)
    print(char_dict)


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

def alpha_chars(dict):
    list_of_chars = []
    for k in dict:
        if k.isalpha():
            list_of_chars.append({"letter": k, "num": dict[k]})
    return list_of_chars[len(list_of_chars) - 1]




main()
