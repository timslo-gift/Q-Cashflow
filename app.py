from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Récupère le port défini par Render
    app.run(host="0.0.0.0", port=port, debug=True)  # Bind à 0.0.0.0 pour Render
