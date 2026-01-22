from fastapi import FastAPI, Query
from keywords_lib import get_keywords, is_keyword

app = FastAPI(title="Python Keywords API")

@app.get("/")
def root():
    return {"message": "Python Keywords REST API"}

# GET all keywords
@app.get("/keywords")
def keywords():
    return {"keywords": get_keywords()}

# Check if word is keyword
@app.get("/keywords/check")
def check_keyword(word: str = Query(..., min_length=1)):
    return {
        "word": word,
        "is_keyword": is_keyword(word)
    }
