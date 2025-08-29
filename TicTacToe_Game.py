# ---------------------------------------------------------------------------#
# TIC-TAC-TOE GAME
# 
# Author: Kevin Garry
# Date: 8/27/2025
# ---------------------------------------------------------------------------#

import tkinter as tk
from tkinter import messagebox

current_player = "X"
buttons = []
board = [' '] * 9
status_label = None


def on_click(index):
    
    global current_player

    if current_player == 'X':
        buttons[index].config(text=current_player, state="disabled", bg="lightblue")

    else:
        buttons[index].config(text=current_player, state="disabled", bg="lightcoral")

    board[index] = current_player

    if check_win(board, current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        status_label.config(text=f"Player {current_player} wins!")
        root.after(1500, reset_game)

    elif ' ' not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        status_label.config(text="It's a draw!")
        root.after(1500, reset_game)

    else:
        current_player = 'O' if current_player == 'X' else 'X'
        status_label.config(text=f"Player {current_player}'s turn")
        

def make_buttons():

    global buttons

    for i in range(9):
        row = i // 3
        col = i % 3
        btn = tk.Button(root, text=" ", font=("Helvetica", 24, "bold"), bg="white", command=lambda i=i: on_click(i))
        btn.grid(row=row, column=col, sticky="nsew")
        buttons.append(btn) # Stores buttons in the buttons list above


def check_win(board, current_player):
    
    for row_start in [0, 3, 6]:
        if board[row_start] == current_player and board[row_start + 1] == current_player and board[row_start + 2] == current_player:
            return True

    for column_start in [0, 1, 2]:
        if board[column_start] == current_player and board[column_start + 3] == current_player and board[column_start + 6] == current_player:
            return True

    if board[0] == board[4] == board[8] == current_player:
        return True

    if board[2] == board[4] == board[6] == current_player:
        return True
    
    return False


def reset_game():

    global board, current_player, status_label

    board = [' '] * 9

    for btn in buttons:
        btn.config(text=" ", state="normal", bg="white", fg="black")
    
    current_player = 'X'
    status_label.config(text="Player X's turn")


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)


make_buttons()

status_label = tk.Label(root, text="Player X's turn", font=("Helvetica", 14))
status_label.grid(row=3, column=0, columnspan=3)


root.mainloop()