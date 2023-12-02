"""
Next day preparation script.
"""

import os
import shutil
import requests

YEAR = 2023


def main(year: str):
    """
    Prepares the next day's folder, including copying the template solution file and
    downloading the input file.
    """
    days_path = os.path.join(os.getcwd(), "years", str(year))
    if not os.path.exists(days_path):
        os.mkdir(days_path)

    days_created = len(os.listdir(days_path))

    if days_created < 25:
        # Create the next day's folder
        os.mkdir(os.path.join(days_path, f"day_{days_created + 1}"))

        # Copy the template solution file
        shutil.copy(
            os.path.join(os.getcwd(), "utils", "solution_template.py"),
            os.path.join(days_path, f"day_{days_created + 1}", "task_1.py"),
        )
        shutil.copy(
            os.path.join(os.getcwd(), "utils", "solution_template.py"),
            os.path.join(days_path, f"day_{days_created + 1}", "task_2.py"),
        )

        # Download the input file from Advent of Code
        url = f"https://adventofcode.com/{year}/day/{days_created + 1}/input"
        headers = headers = {"Cookie": f"session={os.environ['AOC_SESSION']}"}
        response = requests.get(url=url, headers=headers)

        with open(
            os.path.join(days_path, f"day_{days_created + 1}", "test_input.txt"),
            "w",
            encoding="utf-8",
        ) as input_file:
            input_file.write(response.text)

        with open(
            os.path.join(days_path, f"day_{days_created + 1}", "input.txt"),
            "w",
            encoding="utf-8",
        ) as input_file:
            input_file.write(response.text)

    else:
        print("All days created for this year.")


if __name__ == "__main__":
    main(YEAR)
