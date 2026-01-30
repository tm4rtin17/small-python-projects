# Temperature Converter (Celsius ↔ Fahrenheit)

This simple Python program allows users to convert temperatures between **Celsius** and **Fahrenheit** using an interactive command-line menu. It utilizes the [`pyinputplus`](https://pypi.org/project/PyInputPlus/) module for input validation, ensuring the user enters valid numerical values.

---

## Features

- Convert from **Celsius to Fahrenheit**  
- Convert from **Fahrenheit to Celsius**  
- Automatically validates user input to prevent errors  
- Displays the converted value clearly formatted in the console  

---

## Requirements

- Python 3.6 or higher  
- `pyinputplus` library  

To install the required dependency, run:

```bash
pip install pyinputplus
```

---

## Usage

1. Save the script to a file, for example: `temperature_converter.py`
2. Run the program in your terminal or command prompt:

```bash
python temperature_converter.py
```

3. Choose a conversion direction from the menu:
   - `1) Celsius -> Farenheit`
   - `2) Farenheit -> Celsius`
4. Enter the temperature value you want to convert.
5. The program will print the converted temperature.

Example interaction:

```
1) Celsius -> Farenheit
2) Farenheit -> Celsius
Enter a number: 1
Enter a number to convert to Farenheit. 25
25C converts to 77.0F.
```

---

## Notes

- The script uses simple temperature conversion formulas:
  - **Celsius → Fahrenheit:** `F = (C × 1.8) + 32`
  - **Fahrenheit → Celsius:** `C = (F - 32) / 1.8`

---

## Author

Created by *Thomas Martin*  
Last updated: **January 2026**
