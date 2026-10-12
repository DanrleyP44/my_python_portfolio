# Personal Portfolio — Flask

A personal portfolio website built with **Python and Flask** to showcase my programming projects, technical skills, and ongoing journey as a software development student.

The project focuses on presenting my work through a clean, responsive, and straightforward interface while giving me practical experience with Flask and Python web development.

## Live Demo

**Visit the portfolio:** https://my-python-portfolio-vp07.onrender.com/

## About the Project

This portfolio serves as a central place to explore my projects and learn more about my development as a programmer.

Rather than relying on a complex design, the goal is to provide a clear and accessible experience that keeps the focus on the projects themselves.

### Features

- **Project Showcase:** Dedicated sections for my programming projects, including Asteroids and BookBot.
- **Responsive Design:** Layout designed to work across desktop and mobile screens.
- **Clean Interface:** Simple visual hierarchy and consistent styling.
- **Flask Integration:** Python backend serving the portfolio pages.
- **Project Links:** Direct access to project repositories and related resources.

## Technologies

- **Python** — Application logic.
- **Flask** — Web framework.
- **HTML5** — Page structure.
- **CSS3** — Styling and responsive layout.
- **uv** — Python project and dependency management.
- **Git and GitHub** — Version control and source code hosting.

## Featured Projects

### Asteroids

A recreation of the classic Asteroids arcade game, developed in Python using Pygame.

The project helped me practice object-oriented programming, game loops, collision detection, sprite movement, and organizing code into separate classes.

- **Repository:** [DanrleyP44/Asteroids](https://github.com/DanrleyP44/Asteroids)

### BookBot

A Python program that analyzes text files and generates statistical information about their contents.

This project helped me practice file handling, string processing, dictionaries, and basic data analysis.

- **Repository:** [DanrleyP44/book_bot](https://github.com/DanrleyP44/book_bot)

## Getting Started

Follow these instructions to run the portfolio locally.

### Prerequisites

Make sure you have installed:

- Python 3.13 or a compatible version supported by the project.
- [uv](https://docs.astral.sh/uv/).
- Git.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/DanrleyP44/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

Replace `SEU-REPOSITORIO` with the actual repository name.

**2. Install the dependencies**

```bash
uv sync
```

**3. Run the application**

If the project uses `app.py` as its entry point:

```bash
uv run python app.py
```

**4. Open the website**

Visit the local address displayed by Flask in your terminal, usually:

```text
http://127.0.0.1:5000
```

Press `Ctrl + C` in the terminal to stop the development server.

## Project Structure

The exact structure may vary depending on the current implementation. A typical Flask layout looks like this:

```text
portfolio/
├── app.py
├── pyproject.toml
├── uv.lock
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── .gitignore
└── README.md
```

- `app.py` — Initializes Flask and defines application routes.
- `templates/` — Contains HTML templates rendered by Flask.
- `static/` — Stores CSS, JavaScript, and image assets.
- `pyproject.toml` — Defines project metadata and dependencies.
- `uv.lock` — Records resolved dependency versions for reproducible installations.

## What I Learned

Building this project provides practical experience with:

- Creating a web application using Flask.
- Connecting Python routes to HTML templates.
- Organizing static assets and application files.
- Managing dependencies with uv.
- Applying responsive design principles.
- Presenting software projects through a personal portfolio.
- Using Git and GitHub to maintain and share a project.

## Future Improvements

Potential improvements include:

- [ ] Deploy the portfolio to a public hosting platform.
- [ ] Add screenshots or a preview of each project.
- [ ] Improve accessibility and mobile navigation.
- [ ] Add new projects as I continue learning.
- [ ] Refine the application structure as the project grows.

## About Me

I'm a Systems Analysis and Development student interested in Python, backend development, and software engineering.

I'm currently building practical projects to strengthen my programming fundamentals and prepare for my first opportunity as a backend development intern.

- **GitHub:** [@DanrleyP44](https://github.com/DanrleyP44)
- **LinkedIn:** Add your LinkedIn profile URL here.

---

*Built with Python, Flask, and a commitment to continuous learning.*
