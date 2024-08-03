import stockfish
import chess
import tqdm
import cv2
import numpy as np
import math

MATE_SCORE = 100_000
MAX_MATE = 99
BOARD_SIZE = 500

move_cache = dict()

piece_to_name = {
    "P": "Pawn",
    "N": "Knight",
    "B": "Bishop",
    "R": "Rook",
    "Q": "Queen",
    "K": "King",
}

coord_to_square = {
    (0, 0): chess.A1, (0, 1): chess.A2, (0, 2): chess.A3, (0, 3): chess.A4,
    (0, 4): chess.A5, (0, 5): chess.A6, (0, 6): chess.A7, (0, 7): chess.A8,
    (1, 0): chess.B1, (1, 1): chess.B2, (1, 2): chess.B3, (1, 3): chess.B4,
    (1, 4): chess.B5, (1, 5): chess.B6, (1, 6): chess.B7, (1, 7): chess.B8,
    (2, 0): chess.C1, (2, 1): chess.C2, (2, 2): chess.C3, (2, 3): chess.C4,
    (2, 4): chess.C5, (2, 5): chess.C6, (2, 6): chess.C7, (2, 7): chess.C8,
    (3, 0): chess.D1, (3, 1): chess.D2, (3, 2): chess.D3, (3, 3): chess.D4,
    (3, 4): chess.D5, (3, 5): chess.D6, (3, 6): chess.D7, (3, 7): chess.D8,
    (4, 0): chess.E1, (4, 1): chess.E2, (4, 2): chess.E3, (4, 3): chess.E4,
    (4, 4): chess.E5, (4, 5): chess.E6, (4, 6): chess.E7, (4, 7): chess.E8,
    (5, 0): chess.F1, (5, 1): chess.F2, (5, 2): chess.F3, (5, 3): chess.F4,
    (5, 4): chess.F5, (5, 5): chess.F6, (5, 6): chess.F7, (5, 7): chess.F8,
    (6, 0): chess.G1, (6, 1): chess.G2, (6, 2): chess.G3, (6, 3): chess.G4,
    (6, 4): chess.G5, (6, 5): chess.G6, (6, 6): chess.G7, (6, 7): chess.G8,
    (7, 0): chess.H1, (7, 1): chess.H2, (7, 2): chess.H3, (7, 3): chess.H4,
    (7, 4): chess.H5, (7, 5): chess.H6, (7, 6): chess.H7, (7, 7): chess.H8,
}

piece_to_img = {
    "P": [cv2.imread(F"assets/white/p{i}.png") for i in range(2)],
    "N": [cv2.imread(F"assets/white/n{i}.png") for i in range(2)],
    "B": [cv2.imread(F"assets/white/b{i}.png") for i in range(2)],
    "R": [cv2.imread(F"assets/white/r{i}.png") for i in range(2)],
    "Q": [cv2.imread(F"assets/white/q{i}.png") for i in range(2)],
    "K": [cv2.imread(F"assets/white/k{i}.png") for i in range(2)],
    "p": [cv2.imread(F"assets/black/p{i}.png") for i in range(2)],
    "n": [cv2.imread(F"assets/black/n{i}.png") for i in range(2)],
    "b": [cv2.imread(F"assets/black/b{i}.png") for i in range(2)],
    "r": [cv2.imread(F"assets/black/r{i}.png") for i in range(2)],
    "q": [cv2.imread(F"assets/black/q{i}.png") for i in range(2)],
    "k": [cv2.imread(F"assets/black/k{i}.png") for i in range(2)],
    "None": [cv2.imread(F"assets/x{i}.png") for i in range(2)],
}

sf = stockfish.Stockfish(
    path=R"stockfish-16\stockfish\stockfish-windows-x86-64-avx2.exe",
    depth=12,
    parameters={
        "Threads": 6,
        "Hash": 1024,
        # "Minimum Thinking Time": 30,
    }
)

def is_black_turn(bd: chess.Board) -> bool:
    return bd.fen().split()[1] == "b"

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def winrate(bd: chess.Board) -> int:
    m = min(240, len(bd.move_stack)) / 64
    
    return 0.5 + math.tanh(get_ev(bd) * 0.2) * 0.5

def eval2str(ev: float) -> str:
    if abs(ev) < (MATE_SCORE - MAX_MATE) / 100:
        return F"{ev :+06.02f}"

    if ev > 0:
        return F"+M{round(MATE_SCORE - ev * 100)}"

    if ev < 0:
        return F"-M{round(MATE_SCORE + ev * 100)}"

def draw_chessboard(bd: chess.Board, lastmove: None | str=None):
    img = np.zeros((880, 920, 3), dtype=np.uint8)
    
    for i in range(8):
        for j in range(8):
            piece = bd.piece_at(coord_to_square[(j, i)]).__str__()
            
            img[110 * (7 - i):110 * (7 - i) + 110, 110 * j:110 * j + 110, :] = piece_to_img[piece][(i + j) % 2]

    if lastmove is not None:
        cv2.arrowedLine(
            img,
            (110 * (ord(lastmove[0]) - 97) + 55, 110 * (7 - (ord(lastmove[1]) - 49)) + 55),
            (110 * (ord(lastmove[2]) - 97) + 55, 110 * (7 - (ord(lastmove[3]) - 49)) + 55),
            [0, 0, 255],
            5,
        )

    img[round((1 - winrate(bd)) * 880):, 880:920, :] = [255, 255, 255]

    img = cv2.resize(img, (BOARD_SIZE, BOARD_SIZE))
            
    cv2.imwrite("board.png", img)

    cv2.imshow(F"board", img)
    cv2.waitKey(1)

def parse_eval(ev: dict, turn: bool) -> float:
    if ev.get("type") == "cp":
        return ev.get("value") / 100
    
    else:
        if ev.get("value") == 0:
            if turn:
                return -MATE_SCORE / 100
            
            else:
                return MATE_SCORE / 100
            
        if ev.get("value") > 0:
            return (MATE_SCORE - ev.get("value")) / 100
        
        else:
            return (-MATE_SCORE - ev.get("value")) / 100

def _get_ev(bd: chess.Board, turn: bool) -> float:
    sf.set_fen_position(bd.fen())

    return parse_eval(sf.get_evaluation(), turn)

def get_ev(bd: chess.Board) -> float:
    global move_cache

    cv2.waitKey(1)

    if bd.fen() in move_cache:
        return move_cache[bd.fen()]
    
    else:
        ev = _get_ev(bd, not is_black_turn(bd))
        move_cache[bd.fen()] = ev
        return ev
    
def get_moves_with_piece(bd: chess.Board, p: str) -> list[chess.Move]:
    piece = chess.Piece.from_symbol(p)
    # ret = []

    # for i in "abcdefgh":
    #     for j in "12345678":
    #         square_id = ord(i) - 97 + 8 * (ord(j) - 49)
    #         # print(eval(F"chess.{i.upper()}{j}") == ord(i) - 97 + 8 * (ord(j) - 49))

    #         if bd.piece_at(square_id) == piece:
    #             ret.extend([k for k in bd.legal_moves if (str(k)[0], str(k)[1]) == (i, j)])

    # return ret

    return [i for i in bd.legal_moves if bd.piece_at(i.from_square) == piece]

def best_move_with_piece(bd: chess.Board, p: str, rv: bool) -> chess.Move:
    moves = []
    m = get_moves_with_piece(bd, p)
    
    print(F"{'Black' if rv else 'White'} has to move: {piece_to_name.get(p.upper())}")

    if len(m) == 0:
        return None

    for i in tqdm.tqdm(get_moves_with_piece(bd, p)):
        bd.push(i)
        moves.append((i, get_ev(bd)))
        bd.pop()

    moves.sort(key=lambda x: -x[1], reverse=rv)

    print()
    for i in moves:
        # print(F"{bd.san(i[0]) :>10} | {i[1] :+06.02f}")
        print(F"{bd.san(i[0]) :>10} | {eval2str(i[1])}")
    print()

    return moves[0][0]

def fight(white: str, black: str):
    board = chess.Board()
    w_move = list(reversed(white.upper())) * 1_000_000
    b_move = list(reversed(black.lower())) * 1_000_000

    moves = [w_move, b_move]
    turn = True

    move_list = []

    draw_chessboard(board)

    while not board.is_game_over():
        turn = not turn
        while (move := best_move_with_piece(board, moves[turn].pop(), turn)) is None:
            ...

        board.push(move)
        move_list.append(move)

        draw_chessboard(board, lastmove=move.__str__())

    board = chess.Board()

    print(board.result())

    for m in move_list:
        print(board.san(m), end=" ")
        board.push(m)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    bd = chess.Board()

    print(winrate(bd))

    bd.push(chess.Move.from_uci("e2e4"))
    bd.push(chess.Move.from_uci("e7e5"))

    print(winrate(bd))