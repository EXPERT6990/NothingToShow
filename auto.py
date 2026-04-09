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
# Load or initialize JSON
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
else:
    data = {"count": 0, "history": []}

# if last_date < today:
if True:
    # print("No commit today. Updating JSON...")
    i = 0
    while(True):
        print("i : ",i,end='')
        i += 1
        # Prevent duplicate entry
        # if str(today) not in data["history"]:
        if True:
            print("Inside If;")
            data["count"] += 1
            data["history"][0] = str(today)

            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)

            # Commit changes
            repo.git.add(file_path)
            #repo.index.commit(f"{today}")

            try:
                origin = repo.remote(name="origin")
                origin.push()
                print("Auto commit pushed.")
            except Exception as e:
                print("Push failed:", e)
    print("Finished")
else:
    print("Commit already exists today. No action needed.")