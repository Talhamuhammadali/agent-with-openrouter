"""Tests for read file funcitons."""
from functions.read_file import get_file_content

def run_test(*args):
    result = get_file_content(*args)
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    if len(result) < 15000:
        print(result)

def main():
    run_test("calculator", "lorem.txt")
    run_test("calculator", "main.py")
    run_test("calculator", "pkg/calculator.py")
    run_test("calculator", "/bin/cat")
    run_test("calculator", "pkg/does_not_exist.py")

if __name__ == "__main__":
    main()