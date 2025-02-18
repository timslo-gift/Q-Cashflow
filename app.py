from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

import os

port = int(os.environ.get("PORT", 10000))  # Utilise le port défini par Render ou 10000 par défaut
app.run(host="0.0.0.0", port=port)