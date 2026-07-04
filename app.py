from flask import Flask, render_template, request, redirect, url_for, session
from database import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = "change_this_to_a_secure_secret_key"

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = get_db_connection()

    conn.execute(
        "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )

    conn.commit()
    conn.close()

    return render_template("index.html")

@app.route("/admin")
def admin():

    if not session.get("admin"):
        return redirect(url_for("login"))

    conn = get_db_connection()

    messages = conn.execute(
        "SELECT * FROM contacts ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template("admin.html", messages=messages)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "12345":
            session["admin"] = True
            return redirect(url_for("admin"))

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)