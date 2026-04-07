from git import Repo
from datetime import datetime
from collections import Counter

repo = Repo(".")

commits = list(repo.iter_commits())

total_commits = len(commits)

last_commit = commits[0]
last_date = datetime.fromtimestamp(last_commit.committed_date)

authors = [commit.author.name for commit in commits]
author_count = Counter(authors)

print("=== Git Project Insights ===")
print(f"Total commits: {total_commits}")
print(f"Last commit date: {last_date}")

print("\nContributors:")
for author, count in author_count.items():
    print(f"{author}: {count} commits")

# Commit streak (simple version)
dates = sorted(set(datetime.fromtimestamp(c.committed_date).date() for c in commits))
streak = 1

for i in range(1, len(dates)):
    if (dates[i] - dates[i-1]).days == 1:
        streak += 1

print(f"\nApprox commit streak: {streak} days")