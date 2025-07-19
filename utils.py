import base64
import markdown
import requests
import os
from markupsafe import Markup
from cachetools.func import ttl_cache
from datetime import datetime


@ttl_cache(maxsize=50, ttl=86400)
def get_readme(user, repo):
    try:
        headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}", "Accept": "application/vnd.github.v3+json"}
        response = requests.get(f"https://api.github.com/repos/{user}/{repo}/readme",headers=headers)
        if response.status_code == 200:
            data = response.json()
            content = base64.b64decode(data["content"]).decode("utf-8")
            return markdown.markdown(content, extensions=["tables", "fenced_code", "nl2br"])
        else:
            print(f"{response.status_code=}")
    except Exception as e:
        print(f"Error fetching README: {e}")
    return Markup("<p><em>Data not found.</em></p>")


def get_rate_limit():
    try:
        response = requests.get("https://api.github.com/rate_limit")
        if response.status_code == 200:
            data = response.json()
            for key, value in data.items():
                print(key, value, datetime.fromtimestamp(value["core"]["reset"]))
        else:
            print(response.status_code)
    except Exception as e:
        print(f"Error: {e}")


def main():
    get_rate_limit()


if __name__ == "__main__":
    main()
