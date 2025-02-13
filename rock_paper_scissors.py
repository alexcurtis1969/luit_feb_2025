import tkinter as tk
from tkinter import messagebox
from datetime import datetime
class RockPaperScissorsLizardSpock:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors, Lizard, Spock")
        self.create_widgets()
    def create_widgets(self):
        # Player 1 label and dropdown
        player1_label = tk.Label(self.root, text="Player 1:")
        player1_label.grid(row=0, column=0)
        self.player1_var = tk.StringVar(self.root)
        self.player1_var.set("Rock")  # Default choice
        player1_dropdown = tk.OptionMenu(self.root, self.player1_var, "Rock", "Paper", "Scissors", "Lizard", "Spock")
        player1_dropdown.grid(row=0, column=1)
        # Player 2 label and dropdown
        player2_label = tk.Label(self.root, text="Player 2:")
        player2_label.grid(row=1, column=0)
        self.player2_var = tk.StringVar(self.root)
        self.player2_var.set("Rock")  # Default choice
        player2_dropdown = tk.OptionMenu(self.root, self.player2_var, "Rock", "Paper", "Scissors", "Lizard", "Spock")
        player2_dropdown.grid(row=1, column=1)
        # Button to determine the winner
        play_button = tk.Button(self.root, text="Play", command=self.on_click)
        play_button.grid(row=2, columnspan=2)
    def determine_winner(self, player1, player2):
        rules = {
            'Rock': ['Scissors', 'Lizard'],
            'Paper': ['Rock', 'Spock'],
            'Scissors': ['Paper', 'Lizard'],
            'Lizard': ['Spock', 'Paper'],
            'Spock': ['Scissors', 'Rock']
        }
        try:
            if player1 not in rules or player2 not in rules:
                raise ValueError("Invalid choice! Please select again.")
            if player1 == player2:
                return "It's a tie!"
            if player2 in rules[player1]:
                return "Player 1 wins!"
            else:
                return "Player 2 wins!"
        except ValueError as e:
            return str(e)
    def on_click(self):
        def get_current_time():
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        player1_choice = self.player1_var.get()
        player2_choice = self.player2_var.get()
        result = self.determine_winner(player1_choice, player2_choice)
        current_time = get_current_time()
        messagebox.showinfo("Result", f"{result}\n\nGame played at: {current_time}")
def main():
    root = tk.Tk()
    game = RockPaperScissorsLizardSpock(root)
    root.mainloop()
if __name__ == "__main__":
    main()
    