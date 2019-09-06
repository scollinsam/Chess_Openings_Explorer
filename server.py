import bottle
import json
from bottle import route, get, run, template, static_file, post, request, get, jinja2_view
import os
import sys
bottle.TEMPLATE_PATH.insert(0, os.getcwd())
print(bottle.TEMPLATE_PATH.insert(0, os.getcwd()))
print(os.getcwd())
path = sys.path[0]
print(path);

saved_board = {}

pliblib = ["{1: 'rook_black', 2: 'knight_black', 3: 'bishop_black', 4: 'queen_black', 5: 'king_black', 6: 'bishop_black', 7: 'knight_black', 8: 'rook_black', 9: 'pawn_black', 10: 'pawn_black', 11: 'pawn_black', 12: 'pawn_black', 13: 'pawn_black', 14: 'pawn_black', 15: 'pawn_black', 16: 'pawn_black', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty', 21: 'empty', 22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty', 29: 'empty', 30: 'empty', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty', 36: 'empty', 37: 'empty', 38: 'empty', 39: 'empty', 40: 'empty', 41: 'empty', 42: 'empty', 43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'pawn_white', 50: 'pawn_white', 51: 'pawn_white', 52: 'pawn_white', 53: 'pawn_white', 54: 'pawn_white', 55: 'pawn_white', 56: 'pawn_white', 57: 'rook_white', 58: 'knight_white', 59: 'bishop_white', 60: 'queen_white', 61: 'king_white', 62: 'bishop_white', 63: 'knight_white', 64: 'rook_white'}",
          "{1: 'rook_black', 2: 'knight_black', 3: 'bishop_black', 4: 'queen_black', 5: 'king_black', 6: 'bishop_black', 7: 'knight_black', 8: 'rook_black', 9: 'pawn_black', 10: 'pawn_black', 11: 'pawn_black', 12: 'pawn_black', 13: 'pawn_black', 14: 'pawn_black', 15: 'pawn_black', 16: 'pawn_black', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty', 21: 'empty', 22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty', 29: 'empty', 30: 'empty', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty', 36: 'empty', 37: 'empty', 38: 'empty', 39: 'empty', 40: 'empty', 41: 'empty', 42: 'empty', 43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'pawn_white', 50: 'pawn_white', 51: 'pawn_white', 52: 'pawn_white', 53: 'pawn_white', 54: 'pawn_white', 55: 'pawn_white', 56: 'pawn_white', 57: 'rook_white', 58: 'knight_white', 59: 'bishop_white', 60: 'queen_white', 61: 'king_white', 62: 'bishop_white', 63: 'knight_white', 64: 'rook_white'}",
          "{1: 'rook_black', 2: 'knight_black', 3: 'bishop_black', 4: 'queen_black', 5: 'king_black', 6: 'bishop_black', 7: 'knight_black', 8: 'rook_black', 9: 'pawn_black', 10: 'pawn_black', 11: 'pawn_black', 12: 'pawn_black', 13: 'pawn_black', 14: 'pawn_black', 15: 'pawn_black', 16: 'pawn_black', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty', 21: 'empty', 22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty', 29: 'empty', 30: 'empty', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty', 36: 'empty', 37: 'empty', 38: 'empty', 39: 'empty', 40: 'empty', 41: 'empty', 42: 'empty', 43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'pawn_white', 50: 'pawn_white', 51: 'pawn_white', 52: 'pawn_white', 53: 'pawn_white', 54: 'pawn_white', 55: 'pawn_white', 56: 'pawn_white', 57: 'rook_white', 58: 'knight_white', 59: 'bishop_white', 60: 'queen_white', 61: 'king_white', 62: 'bishop_white', 63: 'knight_white', 64: 'rook_white'}",
          "{1: 'rook_black', 2: 'empty', 3: 'bishop_black', 4: 'queen_black', 5: 'king_black', 6: 'bishop_black', 7: 'knight_black', 8: 'rook_black', 9: 'pawn_black', 10: 'pawn_black', 11: 'pawn_black', 12: 'pawn_black', 13: 'empty', 14: 'pawn_black', 15: 'pawn_black', 16: 'pawn_black', 17: 'empty', 18: 'empty', 19: 'knight_black', 20: 'empty', 21: 'empty', 22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty', 29: 'pawn_black', 30: 'empty', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty', 36: 'empty', 37: 'pawn_white', 38: 'empty', 39: 'empty', 40: 'empty', 41: 'empty', 42: 'knight_white', 43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'pawn_white', 50: 'pawn_white', 51: 'pawn_white', 52: 'pawn_white', 53: 'empty', 54: 'pawn_white', 55: 'pawn_white', 56: 'pawn_white', 57: 'rook_white', 58: 'empty', 59: 'bishop_white', 60: 'queen_white', 61: 'king_white', 62: 'bishop_white', 63: 'knight_white', 64: 'rook_white'}",
          "{1: 'rook_black', 2: 'knight_black', 3: 'bishop_black', 4: 'queen_black', 5: 'king_black', 6: 'bishop_black', 7: 'knight_black', 8: 'rook_black', 9: 'pawn_black', 10: 'pawn_black', 11: 'pawn_black', 12: 'pawn_black', 13: 'pawn_black', 14: 'pawn_black', 15: 'pawn_black', 16: 'pawn_black', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty', 21: 'empty', 22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty', 29: 'empty', 30: 'empty', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty', 36: 'empty', 37: 'empty', 38: 'empty', 39: 'empty', 40: 'empty', 41: 'empty', 42: 'empty', 43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'pawn_white', 50: 'pawn_white', 51: 'pawn_white', 52: 'pawn_white', 53: 'pawn_white', 54: 'pawn_white', 55: 'pawn_white', 56: 'pawn_white', 57: 'rook_white', 58: 'knight_white', 59: 'bishop_white', 60: 'queen_white', 61: 'king_white', 62: 'bishop_white', 63: 'knight_white', 64: 'rook_white'}"]
name_lib = ['start', 'norook', 'noknight', 'left knights']
desc_lib = ['This is the board as it appears at the start of a chess match', "This is a board with no black rook", 'this is a game with no kight', 'this is a game in which both players have advanced their left knights']

info = []
def match_check(plib):
    for x in pliblib:
        if x == plib:
            print([name_lib[pliblib.index(x)], desc_lib[pliblib.index(x)]])
            info = [name_lib[pliblib.index(x)], desc_lib[pliblib.index(x)]]
    return info



#print(match_check("{1: 'rook_black', 2: 'knight_black', 3: 'bishop_black', 4: 'queen_black', 5: 'king_black', 6: 'bishop_black', 7: 'knight_black', 8: 'rook_black', 9: 'pawn_black', 10: 'pawn_black', 11: 'pawn_black', 12: 'pawn_black', 13: 'pawn_black', 14: 'pawn_black', 15: 'pawn_black', 16: 'pawn_black', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty', 21: 'empty', 22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty', 29: 'empty', 30: 'empty', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty', 36: 'empty', 37: 'empty', 38: 'empty', 39: 'empty', 40: 'empty', 41: 'empty', 42: 'empty', 43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'pawn_white', 50: 'pawn_white', 51: 'pawn_white', 52: 'pawn_white', 53: 'pawn_white', 54: 'pawn_white', 55: 'pawn_white', 56: 'pawn_white', 57: 'rook_white', 58: 'knight_white', 59: 'bishop_white', 60: 'queen_white', 61: 'king_white', 62: 'bishop_white', 63: 'knight_white', 64: 'rook_white'}"))

@route('/')
def index():
    # print(path)
    return template(path + "/index.html")


@route('/css/<css_file>')
def css(css_file):
    return static_file(css_file, root='css')


@route('/js/<js_file>')
def js(js_file):
    return static_file(js_file, root='js')

@route("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="images")

@post('/save')
def receive_board():
    board = request.json['board']
    for square in board:
        square = int(square)
        saved_board[square] = board[str(square)]
    print(saved_board)
    match_check(str(saved_board))


@get('/getopening')
def send_opening():
    print('it worked')
    matched_board = json.dumps(info)
    return matched_board

def main():
    # print(sys.path)
    run(host='localhost', port=8000)


if __name__ == "__main__":
    main()


