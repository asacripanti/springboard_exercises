def print_upper_words(words):
    for word in words:
        print(word.upper())

def print_upper_words_with_e(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_words_with_set_letters(words, letter):
    for word in words:
        if word.startswith(letter) or word.startswith(letter.upper()):
            print(word.upper())






