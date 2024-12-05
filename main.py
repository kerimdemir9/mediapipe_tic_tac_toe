# import cv2
# import numpy as np
# import mediapipe as mp
#
# # Initialize Mediapipe Hand model
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
#
# # Tic Tac Toe grid parameters
# GRID_SIZE = 3
# CELL_SIZE = 100
# GRID_START_X = 50
# GRID_START_Y = 50
# GRID_END_X = GRID_START_X + GRID_SIZE * CELL_SIZE
# GRID_END_Y = GRID_START_Y + GRID_SIZE * CELL_SIZE
# grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# player = 'X'
# game_over = False
#
#
# # Function to check for winner
# def check_winner():
#     global game_over
#     # Check rows, columns, and diagonals
#     for i in range(GRID_SIZE):
#         if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != "":
#             game_over = True
#             return grid[i][0]
#         if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != "":
#             game_over = True
#             return grid[0][i]
#     if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
#         game_over = True
#         return grid[0][0]
#     if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
#         game_over = True
#         return grid[0][2]
#     return None
#
#
# # Function to draw the grid
# def draw_grid(frame):
#     for i in range(GRID_SIZE + 1):
#         cv2.line(frame, (GRID_START_X + i * CELL_SIZE, GRID_START_Y),
#                  (GRID_START_X + i * CELL_SIZE, GRID_END_Y), (255, 255, 255), 2)
#         cv2.line(frame, (GRID_START_X, GRID_START_Y + i * CELL_SIZE),
#                  (GRID_END_X, GRID_START_Y + i * CELL_SIZE), (255, 255, 255), 2)
#
#
# # Function to draw the marks (X or O)
# def draw_marks(frame):
#     for i in range(GRID_SIZE):
#         for j in range(GRID_SIZE):
#             if grid[i][j] == 'X':
#                 cv2.putText(frame, 'X',
#                             (GRID_START_X + j * CELL_SIZE + 20, GRID_START_Y + i * CELL_SIZE + 80),
#                             cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
#             elif grid[i][j] == 'O':
#                 cv2.putText(frame, 'O',
#                             (GRID_START_X + j * CELL_SIZE + 20, GRID_START_Y + i * CELL_SIZE + 80),
#                             cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)
#
#
# # Function to detect the hovered cell
# def get_hovered_cell(index_finger_x, index_finger_y):
#     if GRID_START_X <= index_finger_x < GRID_END_X and GRID_START_Y <= index_finger_y < GRID_END_Y:
#         col = (index_finger_x - GRID_START_X) // CELL_SIZE
#         row = (index_finger_y - GRID_START_Y) // CELL_SIZE
#         return row, col
#     return None, None
#
#
# # Open the webcam
# cap = cv2.VideoCapture(0)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
#
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#
#             # Extract landmarks for the index finger and thumb
#             index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#
#             # Convert normalized landmarks to pixel coordinates
#             index_finger_x = int(index_finger.x * frame.shape[1])
#             index_finger_y = int(index_finger.y * frame.shape[0])
#             thumb_x = int(thumb_tip.x * frame.shape[1])
#             thumb_y = int(thumb_tip.y * frame.shape[0])
#
#             # Detect hovered cell
#             row, col = get_hovered_cell(index_finger_x, index_finger_y)
#
#             # Highlight hovered cell
#             if row is not None and col is not None:
#                 if grid[row][col] == "":
#                     cv2.rectangle(frame,
#                                   (GRID_START_X + col * CELL_SIZE, GRID_START_Y + row * CELL_SIZE),
#                                   (GRID_START_X + (col + 1) * CELL_SIZE, GRID_START_Y + (row + 1) * CELL_SIZE),
#                                   (0, 255, 0), -1)
#
#             # Check if thumb and index finger are touching
#             distance = np.sqrt((index_finger_x - thumb_x) ** 2 + (index_finger_y - thumb_y) ** 2)
#             if distance < 30 and row is not None and col is not None and grid[row][col] == "":
#                 grid[row][col] = player
#                 player = 'O' if player == 'X' else 'X'
#
#     draw_grid(frame)
#     draw_marks(frame)
#
#     # Check winner
#     winner = check_winner()
#     if winner:
#         cv2.putText(frame, f'{winner} Wins!', (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
#         game_over = True
#
#     cv2.imshow('Tic Tac Toe', frame)
#
#     # Break loop on 'q' key press
#     if cv2.waitKey(1) & 0xFF == ord('q') or game_over:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# below is version 2

# import cv2
# import numpy as np
# import mediapipe as mp
# import time
#
# # Initialize Mediapipe Hand model
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
#
# # Tic Tac Toe grid parameters
# GRID_SIZE = 3
# CELL_SIZE = 150  # Larger cell size
# GRID_START_X = 100
# GRID_START_Y = 100
# GRID_END_X = GRID_START_X + GRID_SIZE * CELL_SIZE
# GRID_END_Y = GRID_START_Y + GRID_SIZE * CELL_SIZE
# grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# player = 'X'
# game_over = False
# menu_open = False
# last_menu_toggle = time.time()
# menu_close_cooldown = time.time()
#
# # Button parameters
# BUTTON_WIDTH = 300
# BUTTON_HEIGHT = 80
# BUTTON_SPACING = 20
# buttons = {
#     "resume": {"x": 250, "y": 200, "text": "Resume"},
#     "new_game": {"x": 250, "y": 300, "text": "New Game"},
#     "quit": {"x": 250, "y": 400, "text": "Quit"},
# }
#
# # Function to check for winner
# def check_winner():
#     global game_over
#     for i in range(GRID_SIZE):
#         if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != "":
#             game_over = True
#             return grid[i][0]
#         if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != "":
#             game_over = True
#             return grid[0][i]
#     if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
#         game_over = True
#         return grid[0][0]
#     if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
#         game_over = True
#         return grid[0][2]
#     return None
#
# # Function to draw the grid
# def draw_grid(frame):
#     for i in range(GRID_SIZE + 1):
#         cv2.line(frame, (GRID_START_X + i * CELL_SIZE, GRID_START_Y),
#                  (GRID_START_X + i * CELL_SIZE, GRID_END_Y), (255, 255, 255), 2)
#         cv2.line(frame, (GRID_START_X, GRID_START_Y + i * CELL_SIZE),
#                  (GRID_END_X, GRID_START_Y + i * CELL_SIZE), (255, 255, 255), 2)
#
# # Function to draw the marks (X or O)
# def draw_marks(frame):
#     for i in range(GRID_SIZE):
#         for j in range(GRID_SIZE):
#             if grid[i][j] == 'X':
#                 cv2.putText(frame, 'X',
#                             (GRID_START_X + j * CELL_SIZE + 40, GRID_START_Y + i * CELL_SIZE + 120),
#                             cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
#             elif grid[i][j] == 'O':
#                 cv2.putText(frame, 'O',
#                             (GRID_START_X + j * CELL_SIZE + 40, GRID_START_Y + i * CELL_SIZE + 120),
#                             cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)
#
# # Function to draw menu
# def draw_menu(frame, hovered_button=None):
#     for key, button in buttons.items():
#         x, y = button["x"], button["y"]
#         color = (0, 255, 0) if key == hovered_button else (0, 255, 255)
#         cv2.rectangle(frame, (x, y), (x + BUTTON_WIDTH, y + BUTTON_HEIGHT), color, -1)
#         cv2.putText(frame, button["text"], (x + 20, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#
# # Function to detect if a point is in a button
# def check_button_press(x, y):
#     for key, button in buttons.items():
#         if button["x"] <= x <= button["x"] + BUTTON_WIDTH and button["y"] <= y <= button["y"] + BUTTON_HEIGHT:
#             return key
#     return None
#
# # Function to detect hovered cell
# def get_hovered_cell(index_finger_x, index_finger_y):
#     if GRID_START_X <= index_finger_x < GRID_END_X and GRID_START_Y <= index_finger_y < GRID_END_Y:
#         col = (index_finger_x - GRID_START_X) // CELL_SIZE
#         row = (index_finger_y - GRID_START_Y) // CELL_SIZE
#         return row, col
#     return None, None
#
# # Open the webcam
# cap = cv2.VideoCapture(0)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     frame = cv2.flip(frame, 1)
#     frame = cv2.resize(frame, (1000, 800))  # Resize frame for larger window
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
#
#     if not menu_open:
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#
#                 # Extract landmarks for the index finger and thumb
#                 index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#                 thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#
#                 # Check fist detection: All fingertips below middle finger MCP
#                 fingers_folded = all(
#                     hand_landmarks.landmark[tip].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
#                     for tip in [mp_hands.HandLandmark.INDEX_FINGER_TIP,
#                                 mp_hands.HandLandmark.RING_FINGER_TIP,
#                                 mp_hands.HandLandmark.PINKY_TIP]
#                 )
#                 if fingers_folded and time.time() - last_menu_toggle > 2:
#                     menu_open = True
#                     last_menu_toggle = time.time()
#                     break
#
#                 # Convert normalized landmarks to pixel coordinates
#                 index_finger_x = int(index_finger.x * frame.shape[1])
#                 index_finger_y = int(index_finger.y * frame.shape[0])
#                 thumb_x = int(thumb_tip.x * frame.shape[1])
#                 thumb_y = int(thumb_tip.y * frame.shape[0])
#
#                 # Detect hovered cell
#                 row, col = get_hovered_cell(index_finger_x, index_finger_y)
#
#                 # Highlight hovered cell
#                 if row is not None and col is not None and grid[row][col] == "":
#                     cv2.rectangle(frame,
#                                   (GRID_START_X + col * CELL_SIZE, GRID_START_Y + row * CELL_SIZE),
#                                   (GRID_START_X + (col + 1) * CELL_SIZE, GRID_START_Y + (row + 1) * CELL_SIZE),
#                                   (0, 255, 0), -1)
#
#                 # Check if thumb and index finger are touching
#                 distance = np.sqrt((index_finger_x - thumb_x) ** 2 + (index_finger_y - thumb_y) ** 2)
#                 if distance < 30 and row is not None and col is not None and grid[row][col] == "":
#                     grid[row][col] = player
#                     player = 'O' if player == 'X' else 'X'
#
#         draw_grid(frame)
#         draw_marks(frame)
#         winner = check_winner()
#         if winner:
#             cv2.putText(frame, f'{winner} Wins!', (150, 600), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
#             menu_open = True
#
#     else:
#         hovered_button = None
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#                 index_finger_x = int(index_finger.x * frame.shape[1])
#                 index_finger_y = int(index_finger.y * frame.shape[0])
#                 hovered_button = check_button_press(index_finger_x, index_finger_y)
#
#                 thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#                 thumb_x = int(thumb_tip.x * frame.shape[1])
#                 thumb_y = int(thumb_tip.y * frame.shape[0])
#                 distance = np.sqrt((index_finger_x - thumb_x) ** 2 + (index_finger_y - thumb_y) ** 2)
#
#                 # Select button if thumb and index finger touch
#                 if distance < 30 and hovered_button:
#                     if hovered_button == "resume":
#                         menu_open = False
#                         menu_close_cooldown = time.time()
#                     elif hovered_button == "new_game":
#                         grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
#                         player = 'X'
#                         game_over = False
#                         menu_open = False
#                         menu_close_cooldown = time.time()
#                     elif hovered_button == "quit":
#                         cap.release()
#                         cv2.destroyAllWindows()
#                         exit()
#
#         draw_menu(frame, hovered_button)
#
#     # Prevent interaction during cooldown
#     if time.time() - menu_close_cooldown < 2:
#         continue
#
#     cv2.imshow('Tic Tac Toe', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
import mediapipe as mp
import time

# Initialize Mediapipe Hand model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Tic Tac Toe grid parameters
GRID_SIZE = 3
CELL_SIZE = 150
GRID_START_X = 100
GRID_START_Y = 100
GRID_END_X = GRID_START_X + GRID_SIZE * CELL_SIZE
GRID_END_Y = GRID_START_Y + GRID_SIZE * CELL_SIZE
grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
player = 'X'
game_over = False
menu_open = False
last_menu_toggle = time.time()
menu_close_cooldown = time.time()
resume_delay = time.time()
winner = None

# Button parameters
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 80
BUTTON_SPACING = 20
buttons = {
    "resume": {"x": 250, "y": 250, "text": "Resume"},
    "new_game": {"x": 250, "y": 350, "text": "New Game"},
    "quit": {"x": 250, "y": 450, "text": "Quit"},
}

# Function to check for winner
def check_winner():
    global game_over
    for i in range(GRID_SIZE):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != "":
            game_over = True
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != "":
            game_over = True
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
        game_over = True
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
        game_over = True
        return grid[0][2]
    return None

# Function to draw the grid
def draw_grid(frame):
    for i in range(GRID_SIZE + 1):
        cv2.line(frame, (GRID_START_X + i * CELL_SIZE, GRID_START_Y),
                 (GRID_START_X + i * CELL_SIZE, GRID_END_Y), (255, 255, 255), 2)
        cv2.line(frame, (GRID_START_X, GRID_START_Y + i * CELL_SIZE),
                 (GRID_END_X, GRID_START_Y + i * CELL_SIZE), (255, 255, 255), 2)

# Function to draw the marks (X or O)
def draw_marks(frame):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 'X':
                cv2.putText(frame, 'X',
                            (GRID_START_X + j * CELL_SIZE + 40, GRID_START_Y + i * CELL_SIZE + 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
            elif grid[i][j] == 'O':
                cv2.putText(frame, 'O',
                            (GRID_START_X + j * CELL_SIZE + 40, GRID_START_Y + i * CELL_SIZE + 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

# Function to draw menu
def draw_menu(frame, hovered_button=None):
    if winner:
        cv2.putText(frame, f'{winner} Wins!', (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
    for key, button in buttons.items():
        x, y = button["x"], button["y"]
        color = (0, 255, 0) if key == hovered_button else (0, 255, 255)
        cv2.rectangle(frame, (x, y), (x + BUTTON_WIDTH, y + BUTTON_HEIGHT), color, -1)
        cv2.putText(frame, button["text"], (x + 20, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Function to detect if a point is in a button
def check_button_press(x, y):
    for key, button in buttons.items():
        if button["x"] <= x <= button["x"] + BUTTON_WIDTH and button["y"] <= y <= button["y"] + BUTTON_HEIGHT:
            return key
    return None

# Function to detect hovered cell
def get_hovered_cell(index_finger_x, index_finger_y):
    if GRID_START_X <= index_finger_x < GRID_END_X and GRID_START_Y <= index_finger_y < GRID_END_Y:
        col = (index_finger_x - GRID_START_X) // CELL_SIZE
        row = (index_finger_y - GRID_START_Y) // CELL_SIZE
        return row, col
    return None, None

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1000, 800))  # Resize frame for larger window
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if time.time() - resume_delay < 2:
        cv2.putText(frame, "Resuming...", (300, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
        cv2.imshow('Tic Tac Toe', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    if not menu_open:
        if results.multi_hand_landmarks and not game_over:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract landmarks for the index finger and thumb
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Check fist detection: All fingertips below middle finger MCP
                fingers_folded = all(
                    hand_landmarks.landmark[tip].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                    for tip in [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                                mp_hands.HandLandmark.RING_FINGER_TIP,
                                mp_hands.HandLandmark.PINKY_TIP]
                )
                if fingers_folded and time.time() - last_menu_toggle > 2:
                    menu_open = True
                    last_menu_toggle = time.time()
                    break

                # Convert normalized landmarks to pixel coordinates
                index_finger_x = int(index_finger.x * frame.shape[1])
                index_finger_y = int(index_finger.y * frame.shape[0])
                thumb_x = int(thumb_tip.x * frame.shape[1])
                thumb_y = int(thumb_tip.y * frame.shape[0])

                # Detect hovered cell
                row, col = get_hovered_cell(index_finger_x, index_finger_y)

                # Highlight hovered cell
                if row is not None and col is not None and grid[row][col] == "":
                    cv2.rectangle(frame,
                                  (GRID_START_X + col * CELL_SIZE, GRID_START_Y + row * CELL_SIZE),
                                  (GRID_START_X + (col + 1) * CELL_SIZE, GRID_START_Y + (row + 1) * CELL_SIZE),
                                  (0, 255, 0), -1)

                # Check if thumb and index finger are touching
                distance = np.sqrt((index_finger_x - thumb_x) ** 2 + (index_finger_y - thumb_y) ** 2)
                if distance < 30 and row is not None and col is not None and grid[row][col] == "":
                    grid[row][col] = player
                    player = 'O' if player == 'X' else 'X'

        draw_grid(frame)
        draw_marks(frame)
        winner = check_winner()
        if winner:
            menu_open = True

    else:
        hovered_button = None
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_finger_x = int(index_finger.x * frame.shape[1])
                index_finger_y = int(index_finger.y * frame.shape[0])
                hovered_button = check_button_press(index_finger_x, index_finger_y)

                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thumb_x = int(thumb_tip.x * frame.shape[1])
                thumb_y = int(thumb_tip.y * frame.shape[0])
                distance = np.sqrt((index_finger_x - thumb_x) ** 2 + (index_finger_y - thumb_y) ** 2)

                # Select button if thumb and index finger touch
                if distance < 30 and hovered_button:
                    if hovered_button == "resume":
                        menu_open = False
                        resume_delay = time.time()
                    elif hovered_button == "new_game":
                        grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
                        player = 'X'
                        game_over = False
                        winner = None
                        menu_open = False
                        resume_delay = time.time()
                    elif hovered_button == "quit":
                        cap.release()
                        cv2.destroyAllWindows()
                        exit()

        draw_menu(frame, hovered_button)

    cv2.imshow('Tic Tac Toe', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
