import keyword

def get_keywords():
    return keyword.kwlist

def is_keyword(word: str) -> bool:
    return keyword.iskeyword(word)
