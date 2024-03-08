def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    #get_word_count(text)
    #get_letter_count(text)
    report(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    text_split = text.split()
    word_count = 0
    for i in range(0, len(text_split)):
        word_count += 1
    return word_count

def get_letter_count(text):
    letter_count = {}
    text_lower = text.lower()
    for letter in text_lower:
        if letter in letter_count and letter.isalpha() == True:
            letter_count[letter] += 1
        elif letter not in letter_count and letter.isalpha() == True:
            letter_count[letter] = 1
    return letter_count

def sort_on(dict):
    return dict["count"]

def report(book, text):
    letters = get_letter_count(text)
    letters_list = []
    for key, value in letters.items():
        new_dict = {"character": key, "count": value}
        letters_list.append(new_dict)
    letters_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book} ---")
    print(f"{get_word_count(text)} words found in the document")
    print("")
    print("")
    for dict in letters_list:
        print(f"The {dict["character"]} character was found {dict["count"]} times")
    print("--- End report ---")

main()