import nltk
from nltk import pos_tag

def validate_words(input_text):
    tagged_text = pos_tag(nltk.word_tokenize(input_text))
    return any(pos.startswith("NN") for word, pos in tagged_text)

def validate_user_input(input_text):

    return validate_words(input_text)

user_input = input("Enter your input: ")
is_valid = validate_user_input(user_input)

if is_valid:
    print("The input is appropriate.")
else:
    print("The input is not appropriate.")