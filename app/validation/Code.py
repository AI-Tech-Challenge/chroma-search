import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

def validate_noun(word):
 
    synsets = wn.synsets(word, pos=wn.NOUN)
    if synsets:
      
        for synset in synsets:
            if word.lower() in synset.lemma_names():
                return True
    return False

def validate_user_input(input_text):

    inappropriate_words = ["explicit_word", "other_inappropriate_word"]

    nouns = [word for word, pos in pos_tag(word_tokenize(input_text)) if pos.startswith('NN')]
    if not nouns:
        return False

    specific_nouns = [noun for noun in nouns if validate_noun(noun.lower()) and noun.lower() not in inappropriate_words]

    if specific_nouns:
        return True
    return False


user_input = input("Enter your input: ")
is_valid = validate_user_input(user_input)

if is_valid:
    print("The input is appropriate.")
else:
    print("The input is not appropriate.")