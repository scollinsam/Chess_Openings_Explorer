import bottle
from bottle import route, get, run, template, static_file, post, request, get, jinja2_view
import os
import sys
bottle.TEMPLATE_PATH.insert(0, os.getcwd())
print(bottle.TEMPLATE_PATH.insert(0, os.getcwd()))
print(os.getcwd())
path = sys.path[0]
print(path);

@route('/')
def index():
    # print(path)
    return template(path + "\\index.html")


@route('/style.css')
def css():
    return static_file('style.css', root='')


@route('/script.js')
def js():
    return static_file("script.js", root='')

@route("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="images")

def main():
    # print(sys.path)
    run(host='localhost', port=8080)


if __name__ == '__main__':
    main()