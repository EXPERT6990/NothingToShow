from git import Repo
from datetime import datetime
import json
import os

repo = Repo(".")
file_path = "./AutoCommitHistory.json"

# Get last commit date
last_commit = repo.head.commit
last_date = datetime.fromtimestamp(last_commit.committed_date).date()
today = datetime.now().date()

if last_date < today:
    print("No commit today. Updating JSON...")

    # Load or initialize JSON
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {"count": 0, "history": []}

    # Prevent duplicate entry
    if str(today) not in data["history"]:
        data["count"] += 1
        data["history"].append(str(today))

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        # Commit changes
        repo.git.add(file_path)
        repo.index.commit(f"Auto commit: inactivity logged for {today}")

        try:
            origin = repo.remote(name="origin")
            origin.push()
            print("Auto commit pushed.")
        except Exception as e:
            print("Push failed:", e)
else:
    print("Commit already exists today. No action needed.")