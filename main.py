"""
Course: CST8002 Programming Language Research Project
Assessment: Practical Project Part 1 - Project Proof of Concept
Professor: [Write Professor Name]
Due Date: [Write Due Date]
Author: Avadh Patel

Description:
    This file is part of a Python proof-of-concept project that reads the
    required course CSV dataset, creates record objects, stores them in a list,
    and displays parsed record data on screen.

References:
    [1] Python Software Foundation, "csv — CSV File Reading and Writing,"
        Python Documentation. [Online]. Available:
        https://docs.python.org/3/library/csv.html. [Accessed: May 31, 2026].
    [2] Python Software Foundation, "Classes," Python Documentation. [Online].
        Available: https://docs.python.org/3/tutorial/classes.html.
        [Accessed: May 31, 2026].
    [3] Python Software Foundation, "Errors and Exceptions," Python Documentation.
        [Online]. Available: https://docs.python.org/3/tutorial/errors.html.
        [Accessed: May 31, 2026].
"""

from pathlib import Path

from src.persistence.csv_loader import load_records


STUDENT_NAME = "Avadh Patel"
DATASET_FILE = Path("data/download.csv")
RECORD_LIMIT = 5


def print_header() -> None:
    """Print the program title and student name so it remains visible."""
    print("=" * 80)
    print("CST8002 Practical Project Part 1 - Project Proof of Concept")
    print(f"Student Name: {STUDENT_NAME}")
    print("=" * 80)


def display_records() -> None:
    """Load records from the dataset and display them on screen."""
    try:
        records = load_records(DATASET_FILE, RECORD_LIMIT)

        print(f"\nLoaded {len(records)} record(s) from: {DATASET_FILE}\n")

        for record in records:
            print(record.display_record())

    except FileNotFoundError:
        print(f"Error: The dataset file was not found: {DATASET_FILE}")
        print("Please check that the CSV file exists inside the data folder.")

    except KeyError as error:
        print(f"Error: Missing expected dataset column: {error}")

    except ValueError as error:
        print(f"Error: A dataset value could not be converted correctly: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


def main() -> None:
    """Run the main program."""
    print_header()
    display_records()


if __name__ == "__main__":
    main()
