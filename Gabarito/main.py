# main.py

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"  # Substitua com sua chave secreta
app.config["DEBUG"] = True
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(message):
    print(f"Mensagem: {message}")
    send(message, broadcast=True)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)  # Alterado para permitir acesso público no GitHub
