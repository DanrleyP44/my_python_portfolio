from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Asteroids",
        "description":(
            "A recreation of the classic arcade game "
            "built with Python and Pygame."
        ),
        "technologies":["Python", "Pygame", "OOP"],
        "github": "https://github.com/DanrleyP44/Asteroids",
    }
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)