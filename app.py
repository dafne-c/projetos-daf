from flask import Flask, render_template, request

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

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados')
def recebedados():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    email = request.args.get('email')
    return render_template('recebedados.html', nome=nome, sobrenome=sobrenome, email=email)

@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade >= 18:
        return 'você é maior de idade'
    else:
        return 'você é menor de idade'

@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('idade.html', idade=idade)

if __name__ == '__main__':
    app.run()