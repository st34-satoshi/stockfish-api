import subprocess

class ChessEngine:
    """
    communicate with stockfish
    """

    def __init__(self) -> None:
        self.p = subprocess.Popen(
            ("/lib/stockfish"),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        self.start_engin()

    def kill(self) -> None:
        self.p.kill()

    def start_engin(self) -> None:
        self.request("uci", "uciok")
        self.request("isready", "readyok")

    def request(self, input_text, expect_response):
        """
        input text and wait until getting expect response
        """
        self.p.stdin.write(f"{input_text}\n".encode())
        self.p.stdin.flush()
        output = ""
        while expect_response != output:
            # output = self.p.stdout.readline
            output = self.p.stdout.readline().decode().strip()

    def best_move(self, moves):
        """
        return {mate: 2, score: 100, best_move: e2e4}
        if lose, mate is minus
        """
        self.p.stdin.write(f"position startpos moves {moves}\n".encode())
        self.p.stdin.write("go depth 20 \n".encode())
        self.p.stdin.flush()
        output = ""
        res = {"mate": None, "score": None, "best_move": None}
        while "bestmove" not in output:
            output = self.p.stdout.readline().decode().strip()
            if "score cp" in output:
                score = output.split('cp ')[1].split(' ')[0]
                res["score"] = score
            if "score mate" in output:
                mate = output.split('mate ')[1].split(' ')[0]
                res["mate"] = mate
            if "bestmove" in output:
                best_move = output.split('bestmove ')[1].split(' ')[0]
                res["best_move"] = best_move
        return res
