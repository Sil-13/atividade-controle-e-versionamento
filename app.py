from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/silvano')
def silvano():
    return render_template('silvano.html')

@app.route('/aluno2')
def aluno2():
    return render_template('aluno2.html')

@app.route('/aluno3')
def aluno3():
    return render_template('aluno3.html')

if __name__ == '__main__':
    app.run(debug=True)  