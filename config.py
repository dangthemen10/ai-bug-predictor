# config.py

import os
from dotenv import load_dotenv
from github import Github

# Tải các biến môi trường từ tệp .env
load_dotenv()

# Lấy giá trị của GITHUB_TOKEN từ môi trường
github_token = os.getenv("GITHUB_TOKEN")

# Kiểm tra nếu token tồn tại
if github_token is None:
    print("Không tìm thấy GITHUB_TOKEN trong tệp .env")
    exit()

# Kết nối với GitHub API
g = Github(github_token)

# Trả về đối tượng Github để sử dụng ở các module khác
def get_github_connection():
    return g
