from fastapi import FastAPI
import logging

logging.basicConfig(filename='log/logger.log', encoding='utf-8', level=logging.INFO)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}