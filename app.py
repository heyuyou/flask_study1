from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route("/hello2/<name>")
@app.route("/hello2")
def hello2(name='he'):
    movies = [
        {"id": 1, "title": 'aaa'},
        {"id": 2, "title": 'bbb'},
        {"id": 3, "title": 'ccc'},
    ]
    return render_template("hello2.html", name=name,movies=movies)


@app.route("/test")
def test():
    print(url_for("hello2"))
    return "test"


if __name__ == '__main__':
    app.run()
