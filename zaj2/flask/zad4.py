from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Witaj w mojej aplikacji Flask!'


@app.route('/about')
def about():
    return 'Zaprogramowano przez Krystian.'


@app.route('/contact')
def contact():
    return 'Email: kchecinski2@o2.com'


if __name__ == '__main__':
    app.run(debug=True)
