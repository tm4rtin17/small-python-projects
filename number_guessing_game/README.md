# Number Guessing Game 🎲

## Overview
This is a simple **Python number guessing game** where the program randomly selects a number between 1 and 20. The player has **five chances** to guess the correct number.

If the guess matches the random number, the player wins; otherwise, the program prompts the user to try again until all guesses are used.

---

## Features
- Random number generation between 1 and 20  
- Five attempts per game  
- Input validation using the `pyinputplus` library  
- Fun, lightweight console gameplay  

---

## Requirements
Make sure you have **Python 3.x** installed, along with the following library:

```bash
pip install pyinputplus
```

---

## How to Play
1. Save the script as `number_guess.py`.  
2. Open a terminal or command prompt in the script directory.  
3. Run the program:

   ```bash
   python number_guess.py
   ```

4. Follow the prompt to guess the number (you get 5 tries).  
5. The program will reveal the correct number when the game ends.

---

## Example Gameplay
```
I'm thinking of a number between 1 and 20. You have 5 guesses.
Guess the number. 10
Try again.
Guess the number. 15
You guessed correctly!
The correct answer was 15. Game over...
```

---

## Notes
- You can customize the number range by changing the values in `random.randint(1, 20)`.  
- Adjust the number of guesses by modifying the range in `for i in range(5)`.
