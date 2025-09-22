from flask import render_template, request, redirect, url_for
from app import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")  # Получаем имя из формы
        email = request.form.get("email")  # Получаем email из формы
        message = request.form.get("message")  # Получаем сообщение из формы
        return render_template("contact.html", name=name, email=email, message=message)
    else:
        return redirect(url_for("contact"))  # Если запрос GET, возвращаем на форму
