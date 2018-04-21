from flask import render_template

from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Gayan"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    data = {
                "title": "Home Page",
                "user": user,
                "posts":posts,
            }

    return render_template("index.html", **data)
