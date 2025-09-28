from flask import render_template, request, redirect, url_for
from app import app
from datetime import datetime


@app.route("/")
def home():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)


@app.route("/about")
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team_members=team_members)


@app.route("/contact")
def contact():
    user_info = {
        'name': 'Alice',
        'address': {
            'street': '123 Main St',
            'city': 'Wonderland',
            'zip': '12345'
        }
    }
    return render_template('contact.html', user=user_info)


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")  # Получаем имя из формы
        email = request.form.get("email")  # Получаем email из формы
        message = request.form.get("message")  # Получаем сообщение из формы
        return render_template("contact.html", name=name, email=email, message=message)
    else:
        return redirect(url_for("contact"))  # Если запрос GET, возвращаем на форму
