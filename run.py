# run.py

from app.find_repos import find_repos
from app.get_bug_commits import get_bug_commits
from app.get_commit_code import get_commit_code

if __name__ == "__main__":
    repo_one = find_repos()
    bug_commits = get_bug_commits(repo_one)

    # Lấy sự khác biệt trong một commit cụ thể
    sha = bug_commits[0]["sha"]
    code_diff = get_commit_code(repo_one, sha)
    for diff in code_diff:
        print(diff)

