import json
import re
from datetime import datetime

import requests


def get_projects(username: str):
    url = f"https://api.github.com/users/{username}/repos"

    # Optional: GitHub token to avoid rate limiting
    # headers = { "Authorization": "token YOUR_GITHUB_TOKEN" }

    response = requests.get(url)  # add headers=headers if using token
    projects_data = []
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            project = {}
            if repo["fork"]:
                continue
            project["display_name"] = " ".join(re.split("[-_]", repo["name"])).title()
            project["name"] = repo["name"]
            project["html_url"] = repo["html_url"]
            project["description"] = repo["description"]
            project["user"] = repo["owner"]["login"]
            project["created_at"] = datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")
            project["updated_at"] = datetime.strptime(repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")
            projects_data.append(project)

        with open("projects_data.json", "w", encoding="utf-8") as f:
            json.dump(projects_data, f, indent=4)

        print("✅ Repository data saved to 'projects_data.json'")
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")


if __name__ == "__main__":
    get_projects("kishandev2509")
