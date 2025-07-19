import base64
import markdown
import requests
from markupsafe import Markup


def get_readme(user, repo):
    try:
        response = requests.get(f"https://api.github.com/repos/{user}/{repo}/readme")
        if response.status_code == 200:
            data = response.json()
            content = base64.b64decode(data["content"]).decode("utf-8")
            return markdown.markdown(content, extensions=["tables", "fenced_code", "nl2br"])
        else:
            print(f"{response.status_code=}")
    except Exception as e:
        print(f"Error fetching README: {e}")
    return Markup("<p><em>Data not found.</em></p>")


def main():
    pass


if __name__ == "__main__":
    main()
