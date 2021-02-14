import re

def remove_trailing_space(sentence):
    return re.sub(' +', ' ', sentence)