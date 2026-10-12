from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "number": "01",
        "category": "PYTHON | GAME DEVELOPMENT",
        "name": "Asteroids",
        "description":(
            "A recreation of the classic arcade game "
            "built with Python and Pygame."
        ),
        "technologies":["Python", "Pygame", "OOP"],
        "github": "https://github.com/DanrleyP44/Asteroids",
    },
    {
        "number": "02",
        "category": "PYTHON · TEXT PROCESSING",
        "name": "BookBot",
        "description": (
            "A command-line program that reads a book from a text file and produces "
            "a report with word and character statistics. A small project focused on "
            "file handling, dictionaries, and breaking a task into functions."
        ),
        "technologies": ["Python", "File I/O", "Dictionaries"],
        "github": "https://github.com/DanrleyP44/book_bot",
    },
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)