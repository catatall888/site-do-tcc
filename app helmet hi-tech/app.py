from flask import Flask, render_template

app = Flask(__name__)

# Rotas principais
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/ia')
def ia():
    return render_template('ia.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/suporte')
def suporte():
    return render_template('suporte.html')

# Página de erro 404 personalizada
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)