import os
import sys

# Make sure this lab's root folder (the parent of "src") is on sys.path, so that
# "from src.lab import problem1" works no matter how this file is launched.

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.lab import problem1


def main():
    result = problem1()
    print(result)


if __name__ == "__main__":
    main()