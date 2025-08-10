import re

import markdown
import requests
from markupsafe import Markup

# from cachetools.func import ttl_cache


# @ttl_cache(maxsize=50, ttl=86400)
def get_readme(user, repo):
    try:
        response = requests.get(f"https://cdn.jsdelivr.net/gh/{user}/{repo}@latest/README.md")
        if response.status_code == 200:
            cdn_base = f"https://cdn.jsdelivr.net/gh/{user}/{repo}@latest/"
            content = response.content.decode("utf-8")
            content = re.sub(r"!\[(.*?)\]\((?!https?://)(.*?)\)", lambda m: f"![{m.group(1)}]({cdn_base}{m.group(2)})", content)
            return markdown.markdown(content, extensions=["tables", "fenced_code", "nl2br"])
        else:
            print(f"{response.status_code=}")
    except Exception as e:
        print(f"Error fetching README: {e}")
    return Markup("<p><em>Data not found.</em></p>")


def get_json_data():
    url = "https://cdn.jsdelivr.net/gh/kishandev2509/githubInfoJson@latest/projects_data.json"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def main():
    print(get_readme("kishandev2509", "Inventory-Management-System"))


if __name__ == "__main__":
    main()
