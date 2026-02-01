# Investment Growth Calculator

This simple Python script calculates the projected value of an investment over time, taking into account an initial investment, regular monthly contributions, and an annual percentage yield (APY). It helps users estimate how their investment might grow year by year.

---

## Features

- Asks the user for:
  - Initial investment amount  
  - Number of years to invest  
  - Monthly contribution amount  
  - Annual Percentage Yield (APY)  
- Calculates compound growth with yearly compounding.
- Displays the final balance after the specified period.

---

## Requirements

- Python 3.7 or higher  
- [PyInputPlus](https://pypi.org/project/PyInputPlus/) module

Install dependencies with:

```bash
pip install pyinputplus
```

---

## How to Run

1. Save the script as `investment_calculator.py`.
2. Open your terminal or command prompt.
3. Run the script with:

   ```bash
   python investment_calculator.py
   ```

4. Follow the prompts to enter:
   - Your initial investment  
   - The number of years to hold the investment  
   - How much you plan to invest monthly  
   - The APY (in percent)

Example session:

```
What is your initial investment? 1000
How many years will you hold your investment? 10
How much will you invest each month? 200
What is your APY(%)? 5
After 10 years, your account would be worth $29703.0.
```

---

## Notes

- Interest compounds yearly.
- Monthly contributions are added annually (12×monthly amount).
- This script doesn’t account for taxes, fees, or inflation.
- For more precise models (e.g., monthly compounding), you can adjust the calculation loop.
