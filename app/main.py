from fastapi import FastAPI, Request
from models.engine import ChessEngine
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(filename='log/logger.log', encoding='utf-8', level=logging.INFO)

app = FastAPI()

origins = [
    "http://chess-database.stu345.com",
    "https://chess-database.stu345.com",
    "http://localhost:8080",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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