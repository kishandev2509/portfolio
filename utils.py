import base64
import markdown
import requests
from markupsafe import Markup


def get_readme(user,repo):
    url = f"https://api.github.com/repos/{user}/{repo}/readme"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        content = base64.b64decode(data["content"]).decode("utf-8")
        html = markdown.markdown(content)
        return Markup(html)
    else:
        return Markup("<p><em>README not available.</em></p>")


def main():
    pass


if __name__ == "__main__":
    main()
