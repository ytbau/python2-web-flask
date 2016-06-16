from flask import Flask, render_template

app = Flask(__name__)

# mkdir templates
# write an index.html file
# browse to http://127.0.0.1:8080/
@app.route("/")
def root():
    return render_template("index.html")

@app.route("/aboutus")
def about():
    return "<p>it is me!</p>"

# browse to http://127.0.0.1:8080/user/Benjamin
@app.route("/user/<username>")
def posted(username):
    return "username is %s" % username

app.run(host = "0.0.0.0", port = 8080, debug = True)