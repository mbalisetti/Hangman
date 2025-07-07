# Hangman Game - Python Console Application

A classic word-guessing game implemented in Python where players try to guess a hidden word letter by letter within a limited number of attempts.

## 🎮 Game Overview

Hangman is a traditional word game where the player attempts to guess a word by suggesting letters within a certain number of attempts. In this implementation, the player can choose word lengths between 3-6 characters, and the number of allowed attempts is calculated as `(2 × word_length) - 2`.

## 🎯 Features

- **Dynamic Word Selection**: Random word selection from a text file database
- **Customizable Difficulty**: Choose word length between 3-6 characters
- **Attempt Management**: Calculated attempts based on word length
- **Input Validation**: Validates alphabetic characters and prevents duplicate guesses
- **Progress Tracking**: Shows current word state, remaining attempts, and previous guesses
- **Replay Option**: Continue playing multiple rounds
- **User-Friendly Interface**: Clear console output with game status updates

## 🛠️ Technology Stack

- **Language**: Python 3.x
- **File I/O**: Text file reading for word database
- **Libraries**: `random` (built-in)

## 📋 Prerequisites

- Python 3.x installed on your system
- Text file named `words-in-code.txt` containing comma-separated words

## 🔧 Installation & Setup

### 1. Clone or Download the Files
```bash
# Download the Python script
# Ensure you have both files in the same directory:
# - hangman.py (the main game file)
# - words-in-code.txt (word database)
```

### 2. Prepare Word Database
Create a file named `words-in-code.txt` with comma-separated words:
```
apple,house,python,computer,table,chair,music,dance,smile,happy,world,peace
```

### 3. Run the Game
```bash
python hangman.py
```

## 🎮 How to Play

1. **Start the Game**: Run the Python script
2. **Choose Word Length**: Enter a number between 3-6 for word length
3. **Make Guesses**: Enter one letter at a time to guess the word
4. **Track Progress**: Monitor your remaining attempts and previous guesses
5. **Win or Lose**: Successfully guess the word or run out of attempts
6. **Play Again**: Choose to start a new round or exit

### Game Rules:
- Word length must be between 3-6 characters
- Number of attempts = (2 × word_length) - 2
- Only alphabetic characters are allowed
- Duplicate guesses are not counted against attempts
- Game ends when word is guessed or attempts are exhausted

## 📁 Project Structure

```
hangman-game/
├── hangman.py              # Main game script
├── words-in-code.txt       # Word database file
└── README.md              # Project documentation
```

## 🎲 Game Functions

### **Core Functions:**

| Function | Description | Parameters |
|----------|-------------|------------|
| `modify(letter, word, fword)` | Updates display word with correctly guessed letter | letter, current word state, target word |
| `fst(length)` | Selects random word of specified length from database | desired word length |
| `dis(length)` | Main game logic handling user input and game flow | word length |

### **Function Details:**

**`modify(letter, word, fword)`**
- Finds position of guessed letter in target word
- Updates the display word to reveal the letter
- Returns updated word string

**`fst(length)`**
- Reads word database from text file
- Randomly selects word matching specified length
- Returns selected word for the game

**`dis(length)`**
- Manages complete game round
- Handles user input and validation
- Tracks attempts and guesses
- Returns final word and attempt count

## 🎯 Sample Gameplay

```
Starting HANGMAN game
enter word length : 5

word : *****
Attempts remaining : 8
previous guesses : []
please enter a guess : a

Letter 'a' is not in the word
word : *****
Attempts remaining : 7
previous guesses : ['a']
please enter a guess : e

Letter 'e' is in the word
word : ***e*
Attempts remaining : 6
previous guesses : ['a', 'e']
...
```

## 🔧 Customization Options

### **Modify Word Database:**
- Edit `words-in-code.txt` to add/remove words
- Ensure words are comma-separated
- Include words of various lengths (3-6 characters)

### **Adjust Difficulty:**
```python
# Change attempt calculation in dis() function
attempts = ((2*length)-2)  # Current formula
# Example alternatives:
attempts = length + 3      # Easier
attempts = length          # Harder
```

### **Extend Word Length Range:**
```python
# Modify validation in main game loop
if(length<3 or length>6):  # Current range
# Change to:
if(length<3 or length>10): # Extended range
```

## 🏆 Resume & Portfolio Points

### **Technical Skills Demonstrated:**

**Programming Concepts:**
- File I/O operations and data parsing
- Random selection algorithms
- String manipulation and processing
- Input validation and error handling
- Loop control and conditional logic
- Function design and modular programming

**Software Development:**
- User interface design for console applications
- Game logic implementation
- Data structure manipulation (lists, strings)
- Exception handling and input validation
- Code organization and documentation

### **Project Highlights:**

• **Console Game Development**: Created interactive Hangman game with dynamic word selection and user-friendly interface

• **File Processing**: Implemented file I/O operations to read and parse word database from external text files

• **Algorithm Implementation**: Developed random word selection algorithm with length filtering and attempt calculation logic

• **Input Validation**: Built comprehensive input validation system preventing invalid characters and duplicate guesses

• **Game State Management**: Designed game flow control with attempt tracking, progress display, and replay functionality

• **String Manipulation**: Utilized advanced string operations for word display updates and character position finding

