🎯 Reverse Guessing Game

A fun Python game where the computer tries to guess the number you think of.

📝 Overview

The Reverse Guessing Game flips the classic guessing concept — you secretly choose a number between 1 and 100, and the computer tries to figure it out.
It guesses smartly by narrowing the range, but still adds randomness to keep each run unpredictable and fun.

This project is perfect for:

practicing Python basics

learning loops & functions

understanding range narrowing logic

making a simple terminal-based game

🚀 Features

✔ User chooses a number (1–100)
✔ Computer guesses intelligently using range shrinking
✔ Randomized guess selection for dynamic gameplay
✔ Tracks number of attempts
✔ Fully validated input
✔ Replay option
✔ Clean, readable code

📂 Project Structure
reverse-guessing-game/
│── main.py
│── README.md
│── .gitignore   (optional)

▶️ How to Run

Make sure Python 3 is installed.

python main.py

📜 Gameplay Example
Choose your number (1-100): 42

Computer guessed correctly in 6 turns!
Your number was: 42

Play again? (yes/no): no
Thanks for playing this game!

🧠 How the Computer Guesses

The game uses two boundaries:

left (starts at 1)

right (starts at 100)

Each attempt:

Computer picks a random number inside the current range.

If guess is too high → reduce right

If too low → increase left

If correct → stop and report attempts

This creates a guessing strategy that feels both smart and playful.
