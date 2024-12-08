from config import get_github_connection

def get_commit_code(repo_name, sha):
    g = get_github_connection()
    repo = g.get_repo(repo_name)
    commit = repo.get_commit(sha)
    files = commit.files

    code_diff = []
    for file in files:
        if file.patch:  # Nếu có thay đổi
            code_diff.append(file.patch)
    return code_diff