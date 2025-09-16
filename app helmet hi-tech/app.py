from flask import Flask, render_template, request, jsonify
import json
import datetime

app = Flask(__name__)

# Simula banco de dados
CHAT_MENSAGENS = []
PERFIL = {
    "nome": "Motociclista Anônimo",
    "bio": "Amante de estrada e velocidade.",
    "foto": "/static/img/avatar.png"
}

ROTA_ENVIADA = None

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")

@app.route("/chat")
def chat():
    return render_template("chat.html", mensagens=CHAT_MENSAGENS)

@app.route("/enviar_mensagem", methods=["POST"])
def enviar_mensagem():
    data = request.get_json()
    mensagem = {
        "usuario": data.get("usuario", "Anônimo"),
        "texto": data.get("texto", ""),
        "horario": datetime.datetime.now().strftime("%H:%M")
    }
    CHAT_MENSAGENS.append(mensagem)
    return jsonify({"status": "ok"})

@app.route("/perfil")
def perfil():
    return render_template("perfil.html", perfil=PERFIL)

@app.route("/salvar_perfil", methods=["POST"])
def salvar_perfil():
    data = request.get_json()
    PERFIL["nome"] = data.get("nome", PERFIL["nome"])
    PERFIL["bio"] = data.get("bio", PERFIL["bio"])
    return jsonify({"status": "ok", "perfil": PERFIL})

@app.route("/suporte")
def suporte():
    return render_template("suporte.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/enviar_rota", methods=["POST"])
def enviar_rota():
    global ROTA_ENVIADA
    data = request.get_json()
    ROTA_ENVIADA = data
    print("📍 Rota recebida para o ESP32:", data)
    return jsonify({"status": "ok", "rota": data})

if __name__ == "__main__":
    app.run(debug=True)