import bottle
from bottle import route, get, run, template, static_file, post, request, get, jinja2_view
import os
import sys
bottle.TEMPLATE_PATH.insert(0, os.getcwd())
print(bottle.TEMPLATE_PATH.insert(0, os.getcwd()))
print(os.getcwd())
path = sys.path[0]
print(path);

saved_board = {}

@route('/')
def index():
    # print(path)
    return template(path + "\\index.html")


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
        saved_board[square] = board[square]
    print(saved_board)
    return board

def main():
    # print(sys.path)
    run(host='localhost', port=8080)


if __name__ == '__main__':
    main()