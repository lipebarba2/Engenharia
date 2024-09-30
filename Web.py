from flask import Flask

app =Flask(__name__)

@app.route('/')
def hello():
    return 'Bem vindo ao back-end simples com Flask'

if __name__ == '__main__':
    app.run(host='localhost', port= 5000)

