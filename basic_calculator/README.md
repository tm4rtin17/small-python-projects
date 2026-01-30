# Calculator.py

A simple, beginner-friendly command-line calculator built in Python.

Supports basic arithmetic operations: addition, subtraction, multiplication, and division.

Uses the excellent `pyinputplus` library for robust, validation-safe user input.

## Features

- Clean numbered menu for choosing operations
- Validates that inputs are integers
- Handles basic arithmetic (+ − × ÷)
- Clear output formatting

## Requirements

- Python 3.6+
- pyinputplus

```bash
pip install pyinputplus
'''

## How to Use

Clone or download the repository
Make sure you have pyinputplus installed
Run the script:
python calculator.py

## Example run:
Enter your first number  42
1. +
2. -
3. *
4. /
Choose an operation (enter a number): 1
Enter your second number  58
The solution is 100.

## Possible Improvements (Ideas for Next Steps)
- Add support for float/decimal numbers
- Add division-by-zero protection
- Allow multiple operations in one session (calculator loop)
- Add more operations (**, %, √, etc.)
- Add history of previous calculations
- Support parentheses / basic expression evaluation
- Add unit tests