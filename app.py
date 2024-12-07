from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

@app.route('/uic')
def uic_func():
    return 'UIC'

@app.route('/uic2')
def uic_func2():
    return 'UIC2'

if __name__ == '__main__':
    app.run(debug=True)