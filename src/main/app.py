import os
import sys

# Make sure this lab's root folder (the parent of "src") is on sys.path, so that
# "from src.main.lab import problem1" works no matter how this file is launched -
# e.g. "python app.py" from inside src/, "python src/app.py" from the lab root, etc.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.main.lab import problem1


def main():
    conn = problem1()
    print("problem1() ran. Run the tests to check whether it's correct.")
    conn.close()


if __name__ == "__main__":
    main()
