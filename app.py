# sse is just a simple HTTP request. Instead of terminating after the server gets the
# request, connection between server and client is kept open for the server to push
# changes to the client
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('example.html')


number_buffer = [i for i in range(100)]


@app.route('/stream')
def stream():
    def event_stream():
        while(len(number_buffer) > 0):
            data = "data:{}\n\n".format(number_buffer.pop())
            yield data
    return Response(event_stream(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True)
