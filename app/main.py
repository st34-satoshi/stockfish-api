from fastapi import FastAPI, Request
from models.engine import ChessEngine
import logging

logging.basicConfig(filename='log/logger.log', encoding='utf-8', level=logging.INFO)

app = FastAPI()

CHESS_ENGINE = ChessEngine()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/analysis")
async def callback(request: Request, position: str):
    logging.info(f'position = {position}')
    logging.info(f'request = {request}')
    CHESS_ENGINE.start_engin()
    # TODO: position is correct?
    res = CHESS_ENGINE.best_move(position)
    # res = CHESS_ENGINE.best_move('rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR b KQkq - 0 1')
    return {"message": "ok", "position": position, "score": res["score"], "mate": res["mate"], "best_move": res["best_move"]}