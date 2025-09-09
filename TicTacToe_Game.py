# ---------------------------------------------------------------------------#
# TIC-TAC-TOE GAME
# 
# Author: Kevin Garry
# Date: 8/27/2025
# ---------------------------------------------------------------------------#

import tkinter as tk
from tkinter import messagebox

# Global variables
current_player = "X"          # Tracks whose turn it is ("X" or "O")
buttons = []                  # Stores references to the 9 button widgets
board = [' '] * 9             # Represents the Tic-Tac-Toe board as a list
status_label = None           # Label widget to show game status

# Handles button clicks for each cell
def on_click(index):
    
    global current_player

    # Update the clicked button's text and color based on current player
    if current_player == 'X':
        buttons[index].config(text=current_player, state="disabled", bg="lightblue")
    else:
        buttons[index].config(text=current_player, state="disabled", bg="lightcoral")

    # Update the board state
    board[index] = current_player

    # Check for a win
    if check_win(board, current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        status_label.config(text=f"Player {current_player} wins!")
        root.after(1500, reset_game)  # Reset the game after 1.5 seconds

    # Check for a draw
    elif ' ' not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        status_label.config(text="It's a draw!")
        root.after(1500, reset_game)

    # Switch player turn
    else:
        current_player = 'O' if current_player == 'X' else 'X'
        status_label.config(text=f"Player {current_player}'s turn")
        
# Creates the 3x3 grid of buttons for the Tic-Tac-Toe board
def make_buttons():
    
    global buttons

    for i in range(9):
        row = i // 3
        col = i % 3
        btn = tk.Button(
            root, text=" ", font=("Helvetica", 24, "bold"), bg="white",
            command=lambda i=i: on_click(i)  # Pass index to handler
        )
        btn.grid(row=row, column=col, sticky="nsew")  # Expand to fill grid
        buttons.append(btn)  # Store button reference

# Checks if the current player has won the game
def check_win(board, current_player):

    # Check rows
    for row_start in [0, 3, 6]:
        if board[row_start] == current_player and board[row_start + 1] == current_player and board[row_start + 2] == current_player:
            return True

    # Check columns
    for column_start in [0, 1, 2]:
        if board[column_start] == current_player and board[column_start + 3] == current_player and board[column_start + 6] == current_player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == current_player:
        return True
    if board[2] == board[4] == board[6] == current_player:
        return True
    
    return False

# Resets the game board and UI to the initial state
def reset_game():
    
    global board, current_player, status_label

    board = [' '] * 9  # Clear board

    # Reset button texts, colors, and state
    for btn in buttons:
        btn.config(text=" ", state="normal", bg="white", fg="black")
    
    current_player = 'X'
    status_label.config(text="Player X's turn")


# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

# Configure grid to expand buttons evenly
for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

# Create buttons
make_buttons()

# Status label to show current player's turn or game result
status_label = tk.Label(root, text="Player X's turn", font=("Helvetica", 14))
status_label.grid(row=3, column=0, columnspan=3)

# Run the Tkinter event loop
root.mainloop()


# ------------------ POTENTIAL ENHANCEMENTS ------------------
# 1. Add a scoreboard to track wins for Player X, Player O, and draws.
# 2. Add a "Restart Game" button so users can reset manually.
# 3. Implement a single-player mode with a simple AI opponent.
# 4. Make the GUI responsive to window resizing and larger screen layouts.
# 5. Add sound effects or animations for button clicks and wins.
# 6. Add logging of game moves to a file to analyze gameplay or debug issues.
# 7. Include color customization or themes for better UX.
