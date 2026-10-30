# Library Management System — Multi-Agent Debugging Challenge

This is a deliberately buggy, multi-file Python project designed to test an autonomous debugging system.

## Project structure

```text
library_management_bug_challenge/
├── main.py
├── requirements.txt
├── library/
│   ├── __init__.py
│   ├── catalog.py
│   ├── loans.py
│   ├── fines.py
│   ├── reports.py
│   └── service.py
└── tests/
    ├── conftest.py
    ├── test_catalog.py
    ├── test_loans.py
    ├── test_fines.py
    └── test_reports.py
```

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -v
python main.py
```

## Challenge notes

The project contains intentional defects in title search, last-copy borrowing, overdue fine calculation, and overdue reporting. Some tests pass so the debugger must distinguish correct behavior from broken behavior. Do not delete or weaken tests to make the suite pass.

The correct target is to fix the source modules while preserving their public APIs and the package structure.
