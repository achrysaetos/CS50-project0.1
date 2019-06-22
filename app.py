from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user", methods=["POST"])
def user():
    name=request.form.get("name")
    name2=request.form.get("name2")
    if name=="username" and name2=="password":
        return render_template("login.html")
    else:
        return render_template("register.html")

@app.route("/newuser", methods=["GET"])
def newuser():
    return render_template("register.html")

@app.route("/olduser", methods=["GET"])
def olduser():
    return render_template("register.html")

@app.route("/blog", methods=["GET"])
def blog():
    return render_template("blog.html")
