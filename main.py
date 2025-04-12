from fastapi import FastAPI
from pydantic import BaseModel
from scoring import analyze_article  # <-- this must match exactly

app = FastAPI()

class ArticleRequest(BaseModel):
    content: str

@app.post("/analyze")
async def analyze(request: ArticleRequest):
    # analyze_article is async, so we await it
    result = await analyze_article(request.content)
    return result
