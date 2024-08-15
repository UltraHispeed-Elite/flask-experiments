from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello world")
    return "<script>console.log('hello world');</script>"


app.run(debug=True, port=8001)