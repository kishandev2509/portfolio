from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

from utils import get_json_data, get_readme

app = Flask(__name__)


@app.context_processor
def inject_data():
    return {
        "current_year": datetime.now().year,
        "github_username": "kishandev2509",
        "social_links": {
            "GitHub": "https://github.com/kishandev2509",
            "LinkedIn": "https://linkedin.com/in/kishandev2509",
            "EmailMe": "mailto:kishandevprajapati4@gmail.com",
        },
        "nav_links": {
            "Home": url_for("home"),
            "About": url_for("about"),
            "Projects": url_for("projects"),
            "Contact": url_for("contact"),
        },
        "quick_links": {
            "About": url_for("about"),
            "Contact": url_for("contact"),
        },
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    projects_data = get_json_data()
    return render_template("projects.html", projects=projects_data)


@app.route("/projects/<user>")
def profile_page(user):
    repo = user
    content = get_readme(user, repo)
    return render_template("readme.html", content=content, user=user, repo="")


@app.route("/projects/<user>/<repo>")
def project_repo(user, repo):
    if user == repo:
        return redirect(url_for("profile_page", user=user))
    content = get_readme(user, repo)
    return render_template("readme.html", content=content, user=user, repo=repo)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Optional: handle or store the message (e.g., email, DB, file, etc.)
        print(f"Message from {name} ({email}): {message}")

        return render_template("contact.html", success=True)

    return render_template("contact.html", success=False)


if __name__ == "__main__":
    app.run(debug=True)
