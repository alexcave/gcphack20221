from flask import Flask, render_template

app = Flask(__name__)


def index():
    return render_template('index.html')


app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
