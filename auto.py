from git import Repo
from datetime import datetime
import json
import os
import subprocess

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
    i = data["count"]
    while(True):
        print("i : ",i,end='')
        i += 1
        # Prevent duplicate entry
        # if str(today) not in data["history"]:
        if True:
            print("Inside If;")
            data["count"] = i
            data["history"][0] = str(i)

            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)

            # Commit changes
            subprocess.run(["git", "add", file_path], check=True)
            subprocess.run(["git", "commit", "-m", f"{i}"], check=True)

            # # Push only every 10 commits to speed up
            # if i % 10 == 0:
            #     try:
            #         subprocess.run(["git", "push", "origin", "main"], check=True)
            #         print("Auto commit pushed.")
            #     except subprocess.CalledProcessError as e:
            #         print("Push failed:", e)
            # Push remaining commits at the end
            
            try:
                subprocess.run(["git", "push", "origin", "main"], check=True)
                print("Final push completed.")
            except subprocess.CalledProcessError as e:
                print("Final push failed:", e)
    print("Finished")
else:
    print("Commit already exists today. No action needed.")