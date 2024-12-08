from config import get_github_connection

def find_repos():
    g = get_github_connection()
    # Tìm các repository phổ biến viết bằng Python
    repositories = g.search_repositories(query="language:Python stars:>500")
    repo_names = []
    for repo in repositories[:5]:  # Lấy 5 repo đầu tiên
        print(f"Repo Name: {repo.full_name}, Stars: {repo.stargazers_count}")
        repo_names.append(repo.full_name)

    print(f"Repo Name: {repo_names}")
    return repo_names[1]
