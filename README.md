

# Hand-Controlled Tic Tac Toe Game

This project implements a hand-gesture-controlled Tic Tac Toe game using Python and the Mediapipe, OpenCV, and NumPy libraries. Players can interact with the game grid and menu options using their hand gestures.

---

## Installation

Before running the script, ensure that you have Python 3 installed. Install the required dependencies by running:

```bash
pip install opencv-python mediapipe numpy
```

---

## How to Run

1. Make sure your webcam is connected.

2. Start the game by running the script:
   
   ```bash
   python3 main.py
   ```

---

## How It Works

### Hand Gesture Controls:

- **Menu Navigation:**
  - Open the menu by making a fist (all fingertips below the middle finger's MCP joint).
  - Use your index finger to hover over a button in the menu.
  - Touch your index finger and thumb together to select a button (e.g., Resume, New Game, Quit).
- **Playing the Game:**
  - Use your index finger to hover over a cell in the Tic Tac Toe grid.
  - Touch your index finger and thumb together to mark the selected cell with your symbol ('X' or 'O').

### Game Rules:

- Standard Tic Tac Toe rules apply: players take turns marking the grid. The first to align three symbols horizontally, vertically, or diagonally wins. A full grid without a winner results in a tie.

---

## Features

- **Interactive Grid:** A 3x3 Tic Tac Toe board is drawn in the center of the screen, with cells highlighted when hovered.
- **Hand Gesture Detection:** Mediapipe's hand landmarks are used to detect gestures and interactions.
- **Menu Options:** Resume, start a new game, or quit via hand gestures.
- **Real-Time Feedback:** Displays the current player's turn and declares the winner or tie at the end of the game.

---

## Known Issues

- The game requires a well-lit environment for accurate hand detection.
- Performance may vary depending on webcam quality.

---

## Quit the Game (without gestures/menu)

Press the **'q' key** to exit at any time.

---


