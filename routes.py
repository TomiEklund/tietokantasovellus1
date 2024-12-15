from app import app
import messages, users
from db import db
from flask import session
from sqlalchemy.sql import text
from flask import render_template, request, redirect, abort

@app.route("/")
def index():
    list = messages.get_messages()
    return render_template("index.html", messages=list)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.check_user(username)==True:
            return render_template("error.html", message="Käyttäjänimi varattu, keksi uusi")
        if len(username)<5 or len(password1)<5:
            return render_template("error.html", message="Käyttäjänimen ja salasanan tulee olla yli 4 merkkiä")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/newpost", methods=["GET", "POST"])
def send():
    if request.method == "GET":
        return render_template("newpost.html")
    if request.method == "POST":
        header= request.form["header"]
        content = request.form["content"]
        if users.user_id() == 0:
            return render_template("error.html", message="Kirjaudu sisään, jotta voit lähettää viestejä")
        elif len(header)<4 or len(header)>30:
            return render_template("error.html", message="Otsikon pitää olla 3-30 merkkiä")
        elif len(content)<4 or len(content)>300:
            return render_template("error.html", message="Viestin pitää olla 3-300 merkkiä")
        elif messages.send(header, content):
            return redirect("/")
        elif session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/mymessages")
def mymessages():
    list = messages.my_messages()
    return render_template ("mymessages.html", messages=list)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/result")
def result():
    query = request.args["query"]
    sql = text("SELECT M.header, M.content, U.username, M.sent FROM messages M, Users U WHERE content LIKE :query OR header LIKE :query AND M.user_id=U.id")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    messages = result.fetchall()
    if len(messages)==0:
        return render_template("error.html", message="Käyttämäsi hakusana ei esiinny viesteissä tai otsikoissa")
    return render_template("result.html", messages=messages)