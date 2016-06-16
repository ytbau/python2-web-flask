from flask import Flask

# construct flask web app
app = Flask(__name__);

# slash is the root url for the local pc
@app.route("/")
def hello():
    return "Hello, World!";

app.run(host = "0.0.0.0", port = 8080, debug = True);

# PyScripter toolbar > click Run
# browse to http://127.0.0.1:8080

# notes:
# install python2 compiler
# install pyscripter ide
# install pip for installing python libraries
# install setuptools
# linux$ sudo pip install flask



