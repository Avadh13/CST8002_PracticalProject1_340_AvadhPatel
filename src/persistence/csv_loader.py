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

import csv
from pathlib import Path
from typing import List

from src.model.production_record import ProductionRecord


def load_records(file_path: Path, record_limit: int = 5) -> List[ProductionRecord]:
    """Read the CSV dataset and create a list of ProductionRecord objects.

    Args:
        file_path (Path): Path to the CSV dataset.
        record_limit (int): Maximum number of records to load.

    Returns:
        List[ProductionRecord]: A list of parsed record objects.

    Raises:
        FileNotFoundError: If the dataset file does not exist.
        ValueError: If a required numeric value cannot be converted.
        KeyError: If a required dataset column is missing.
    """
    records: List[ProductionRecord] = []

    with file_path.open(mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row_number, row in enumerate(reader, start=1):
            if row_number > record_limit:
                break

            record = ProductionRecord(
                CSDUID=row["CSDUID"],
                CSD=row["CSD"],
                Period=int(row["Period"]),
                IndicatorSummaryDescription=row["IndicatorSummaryDescription"],
                UnitOfMeasure=row["UnitOfMeasure"],
                OriginalValue=float(row["OriginalValue"]),
            )

            records.append(record)

    return records
