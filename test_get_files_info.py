"""Test for file info fetch tool."""
from functions.list_files import get_file_info

def main():
    print(get_file_info("calculator", "."))
    print(get_file_info("calculator", "pkg"))
    print(get_file_info("calculator", "../"))
    print(get_file_info("calculator", "/bin"))

if __name__ == "__main__":
    main()