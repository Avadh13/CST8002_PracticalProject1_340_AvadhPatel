"""
Course: CST8002 Programming Language Research Project
Assessment: Practical Project 1
Author: Avadh Patel


References:
    [1] Python Software Foundation, "csv — CSV File Reading and Writing,"
        Python Documentation. https://docs.python.org/3/library/csv.html
    [2] Python Software Foundation, "Classes," Python Documentation.
        https://docs.python.org/3/tutorial/classes.html
    [3] Python Software Foundation, "Errors and Exceptions," Python Documentation.
        https://docs.python.org/3/tutorial/errors.html
"""

import csv
from dataclasses import dataclass
from pathlib import Path


# -----------------------------
# Program settings
# -----------------------------
STUDENT_NAME = "Avadh Patel"
CSV_FILE = Path("data/download.csv")
RECORD_LIMIT = 5


# -----------------------------
# Model class
# -----------------------------
@dataclass
class ProductionRecord:
    """Stores one row from the CSV file."""

    csduid: str
    csd: str
    period: int
    indicator: str
    unit: str
    original_value: float

    def display(self) -> str:
        """Return one record as a clean readable line."""
        return (
            f"CSDUID: {self.csduid} | "
            f"CSD: {self.csd} | "
            f"Period: {self.period} | "
            f"Indicator: {self.indicator} | "
            f"Unit: {self.unit} | "
            f"Original Value: {self.original_value}"
        )


# -----------------------------
# File reading function
# -----------------------------
def load_records(file_path: Path, limit: int) -> list[ProductionRecord]:
    """Read the CSV file and return a list of ProductionRecord objects."""
    records = []

    with file_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=1):
            if row_number > limit:
                break

            record = ProductionRecord(
                csduid=row["CSDUID"],
                csd=row["CSD"],
                period=int(row["Period"]),
                indicator=row["IndicatorSummaryDescription"],
                unit=row["UnitOfMeasure"],
                original_value=float(row["OriginalValue"]),
            )

            records.append(record)

    return records


# -----------------------------
# Display functions
# -----------------------------
def print_header() -> None:
    """Print project title."""
    print("=" * 80)
    print("CST8002 Practical Project Part 1 - Project Proof of Concept")
    print(f"Student Name: {STUDENT_NAME}")
    print("=" * 80)


def run_program() -> None:
    """Run the full program."""
    print_header()

    try:
        records = load_records(CSV_FILE, RECORD_LIMIT)

        print(f"\nLoaded {len(records)} record(s) from: {CSV_FILE}\n")

        for record in records:
            print(record.display())

    except FileNotFoundError:
        print(f"Error: CSV file was not found: {CSV_FILE}")
        print("Make sure download.csv is inside the data folder.")

    except KeyError as error:
        print(f"Error: Missing required CSV column: {error}")

    except ValueError as error:
        print(f"Error: Could not convert a number correctly: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


# -----------------------------
# Program starts here
# -----------------------------
if __name__ == "__main__":
    run_program()
