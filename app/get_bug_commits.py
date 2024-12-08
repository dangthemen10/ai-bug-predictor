
from config import get_github_connection

def get_bug_commits(repo_name):
    g = get_github_connection()
    repo = g.get_repo(repo_name)
    commits = repo.get_commits()
    bug_commits = []

    for commit in commits:
        message = commit.commit.message.lower()
        if "fix" in message or "bug" in message:
            bug_commits.append({
                "sha": commit.sha,
                "message": commit.commit.message,
                "date": commit.commit.author.date
            })
    return bug_commits


