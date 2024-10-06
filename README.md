# Cron-Parser

A simple command line application to parse cron string regex and print the schedules at which the job will run.

Supported time fields:
 - Minute
 - Hour
 - Day
 - Month
 - Day of the Week

## Requirements

- Python >= 3.10
- Github

## Setup

1. Clone the package 

```
gh repo clone sayali27/Cron-Regex-Parser
```

2. Install the parser package

```
pip install --editable .
```

3. Install `pytest` to run tests

```
pip install -U pytest
```

## Usage

### 1. Run the parser

```
$ parse "*/6 1,5-7 1-3,7 5 * pwd"
```

Output:

```
minutes       0 6 12 18 24 30 36 42 48 54
hour          1 5 6 7
day of month  1 2 3 7
month         5
day of week   1 2 3 4 5 6 7
command       pwd
```

### 2. Run the tests

```
$ pytest tests/test_parser.py
```