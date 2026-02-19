from flask import Flask, render_template
import socket
import os

app = Flask(__name__)

VERSION = os.getenv("VERSION", "unknown")

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return render_template("index.html", hostname=hostname, version=VERSION)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
