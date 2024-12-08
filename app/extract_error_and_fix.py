import difflib

def extract_error_and_fix(before_code, after_code):
    diff = difflib.unified_diff(
        before_code.splitlines(), after_code.splitlines(), lineterm=""
    )
    error_lines = []
    fix_lines = []

    for line in diff:
        if line.startswith("-"):
            error_lines.append(line[1:])
        elif line.startswith("+"):
            fix_lines.append(line[1:])

    return "\n".join(error_lines), "\n".join(fix_lines)

# Ví dụ dữ liệu trước và sau sửa lỗi
before_code = """def divide(a, b): return a / b"""
after_code = """def divide(a, b): return a / b if b != 0 else 0"""

error, fix = extract_error_and_fix(before_code, after_code)
print("Error Code:\n", error)
print("Fixed Code:\n", fix)
