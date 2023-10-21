from fastapi import FastAPI, Request
from models.engine import ChessEngine
import logging

logging.basicConfig(filename='log/logger.log', encoding='utf-8', level=logging.INFO)

app = FastAPI()

CHESS_ENGINE = ChessEngine()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/analysis")
async def analysis(request: Request, moves: str = "e2e4 e7e5"):
    logging.info(f'position = {moves}')
    logging.info(f'request = {request}')
    # TODO: position is correct?
    res = CHESS_ENGINE.best_move(moves)
    return {"message": "ok", "moves": moves, "score": res["score"], "mate": res["mate"], "best_move": res["best_move"]}