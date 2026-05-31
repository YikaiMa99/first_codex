from datetime import datetime
import os
import sys


def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Hello, Codex!")
    print(f"Python version: {sys.version}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Current time: {current_time}")


if __name__ == "__main__":
    main()
