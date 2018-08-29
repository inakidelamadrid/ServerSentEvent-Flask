# sse is just a simple HTTP request. Instead of terminating after the server gets the
# request, connection between server and client is kept open for the server to push
# changes to the client
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('example.html')


if __name__ == "__main__":
    app.run(debug=True)
