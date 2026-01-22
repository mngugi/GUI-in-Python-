import keyword

def get_keywords():
    return keyword.kwlist

def is_keyword(word):
    return keyword.iskeyword(word)
