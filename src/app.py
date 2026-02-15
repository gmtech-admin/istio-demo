from flask import Flask
import socket
import os

app = Flask(__name__)

VERSION = os.getenv("VERSION", "unknown")

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"Version: {VERSION} | Host: {hostname}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
