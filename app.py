from flask import Flask, url_for

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route("/hello2/<name>")
@app.route("/hello2")
def hello2(name='he'):
    return "hello %s" % name


@app.route("/test")
def test():
    print(url_for("hello2"))
    return "test"


if __name__ == '__main__':
    app.run()
