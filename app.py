from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aluno1')
def aluno1():
    return render_template('aluno1.html')

@app.route('/aluno2')
def aluno2():
    return render_template('aluno2.html')

@app.route('/aluno3')
def aluno3():
    return render_template('aluno3.html')

if __name__ == '__main__':
    app.run(debug=True)  