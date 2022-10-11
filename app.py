from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key="donotguessyouwillbeafraid"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signIn():
    username = request.form["username"]
    pwd = request.form["pwd"]
    if(username and pwd):
        if (username == "test" and pwd =="test"):
            session["login"] = "success"
            return redirect("/member")
        else:
            session["login"] = "fail"
            return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
    else:
        session["login"] = "fail"
        return redirect(url_for("error", message="請輸入帳號、密碼"))

@app.route("/member")
def member():
    if (session["login"] == "success"):
       return render_template("member.html")
    return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", mes=message)

@app.route("/calculate")
def cal():
    value = request.args.get("value")
    return 

@app.route("/square/<value>")
def mathPow(value):
    return render_template("calculate.html", result=str(pow(int(value),2)))

@app.route("/signout")
def signOut():
    session["login"] = "fail"
    return render_template("index.html")       

app.run(port=3000)