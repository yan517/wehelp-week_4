from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signIn():
    username = request.form["username"]
    pwd = request.form["pwd"]
    if(username and pwd):
        if (username == "test" and pwd =="test"):
            resp = make_response(redirect("/member"))
            resp.set_cookie('login', 'success', secure=True)
            return resp
        else:
            resp = make_response(redirect(url_for("error", message="帳號、或密碼輸入錯誤")))
            resp.set_cookie('login', 'fail', secure=True)
            return resp
    else:
        resp = make_response(redirect(url_for("error", message="請輸入帳號、密碼")))
        resp.set_cookie('login', 'fail', secure=True)
        return resp

@app.route("/member")
def member():
    if (request.cookies.get('login') == "success"):
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
    resp = make_response(render_template("index.html"))
    resp.set_cookie('login', 'fail', secure=True)
    return resp   

app.run(port=3000)