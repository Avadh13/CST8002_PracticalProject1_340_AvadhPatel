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

from dataclasses import dataclass


@dataclass
class ProductionRecord:
    """Represents one parsed record from the CST8002 CSV dataset.

    The field names intentionally match the dataset column names:
    CSDUID, CSD, Period, IndicatorSummaryDescription, UnitOfMeasure,
    and OriginalValue.
    """

    CSDUID: str
    CSD: str
    Period: int
    IndicatorSummaryDescription: str
    UnitOfMeasure: str
    OriginalValue: float

    def display_record(self) -> str:
        """Return a formatted string containing this record's information.

        Returns:
            str: A readable one-line summary of the record.
        """
        return (
            f"CSDUID: {self.CSDUID} | "
            f"CSD: {self.CSD} | "
            f"Period: {self.Period} | "
            f"Indicator: {self.IndicatorSummaryDescription} | "
            f"Unit: {self.UnitOfMeasure} | "
            f"Original Value: {self.OriginalValue}"
        )
