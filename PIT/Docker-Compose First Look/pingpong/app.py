from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def ping():
    pong_response = os.getenv("PONG", "Default Pong")
    return f"Pong: {pong_response}"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    