from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/contato")
def contato():
    dados = {'nome' : 'dafne', 'email' : 'c.dafne@escolar.ifrn.edu.br'}
    return render_template('contato.html', dados=dados)

@app.route("/disciplinas")
def disciplinas():
    return render_template('disciplinas.html')

@app.route("/curriculo")
def curriculo():
    return render_template('curriculo.html')

@app.route('/usuario', defaults={'nome' : 'desconhecido', 'sobrenome' : 'desconhecido'})
@app.route('/usuario/<nome>/<sobrenome>/')
def usuario(nome, sobrenome):
    info = {'nome' : nome, 'sobrenome' : sobrenome}
    return render_template('usuario.html', info=info)

@app.route('/semestre/<int:x>')
def semestre(x):
    atual = x
    anterior = x - 1
    return render_template('semestre.html', atual=atual, anterior=anterior)

if __name__ == '__main__':
    app.run()