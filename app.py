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

@app.route('/verificaridade/', defaults={'idade': None})
@app.route('/verificaridade/<int:idade>')
def verificaridade2(idade):
    return render_template('verificaridade2.html', idade=idade)

@app.route('/exemplolaco')
def exemplolaco():
    return render_template('exemplolaco.html')

@app.route('/lista')
def lista():
    return render_template('lista.html', itens=itens)

@app.route('/produtos')
def produtos():
    itens = [
        { 'nome' : 'teclado', 'preco' : 200, 'categoria' : 'computador' },
        { 'nome' : 'pen-drive', 'preco' : 50, 'categoria' : 'celular' },
        { 'nome' : 'smartphone', 'preco' : 4500, 'categoria' : 'computador' }
    ]
    return render_template('produtos.html', itens=itens)

if __name__ == '__main__':
    app.run()