# CST8002 Practical Project Part 1 - Project Proof of Concept

Student: Avadh Patel

## Project Description

This Python project reads the required CST8002 CSV dataset, creates record objects, stores them in a list, and displays parsed records on screen.

## Dataset Used

The dataset file is stored here:

```text
data/download.csv
```

The program uses the dataset column names directly in the source code:

- CSDUID
- CSD
- Period
- IndicatorSummaryDescription
- UnitOfMeasure
- OriginalValue

## Project Structure

```text
CST8002_PracticalProject_Project1_AvadhPatel/
├── data/
│   └── download.csv
├── src/
│   ├── model/
│   │   ├── __init__.py
│   │   └── production_record.py
│   └── persistence/
│       ├── __init__.py
│       └── csv_loader.py
├── main.py
├── README.md
└── .gitignore
```

## How to Run

Open the project folder in VS Code or terminal and run:

```bash
python main.py
```

If `python` does not work on Windows, try:

```bash
py main.py
```

## Features Demonstrated

- Variables
- Methods/functions
- Loop structure
- File-IO
- Exception handling
- Built-in library usage
- List data structure
- Object-oriented programming
- Separate source code files and folders
"# CST8002_PracticalProject1_340_AvadhPatel" 
