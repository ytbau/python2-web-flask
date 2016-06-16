from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>hello world</p>"

@app.route("/aboutus") # another url on address bar
def about():
    return "<p>it is me!</p>"

app.run(host = "0.0.0.0", port = 8080, debug = True)

# browse to http://127.0.0.1:8080/aboutus