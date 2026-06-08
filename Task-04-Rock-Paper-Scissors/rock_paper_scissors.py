import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft Rock-Paper-Scissors")
        self.root.geometry("450x550")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        # Game Scores
        self.user_score = 0
        self.computer_score = 0

        # Title Label
        title_label = tk.Label(
            root, text="ROCK-PAPER-SCISSORS", font=("Helvetica", 16, "bold"), bg="#1a1a2e", fg="#e94560"
        )
        title_label.pack(pady=20)

        # Score Board Frame
        score_frame = tk.Frame(root, bg="#161625", bd=1, relief="solid")
        score_frame.pack(pady=10, padx=40, fill="x")

        self.score_label = tk.Label(
            score_frame, 
            text="You: 0   |   Computer: 0", 
            font=("Helvetica", 14, "bold"), 
            bg="#161625", 
            fg="#ffffff",
            pady=10
        )
        self.score_label.pack()

        # Display Action/Status Label
        self.status_label = tk.Label(
            root, 
            text="Choose your move to start the game!", 
            font=("Helvetica", 12, "italic"), 
            bg="#1a1a2e", 
            fg="#8186a0"
        )
        self.status_label.pack(pady=20)

        # Results Display Board
        self.result_label = tk.Label(
            root, 
            text="", 
            font=("Helvetica", 14, "bold"), 
            bg="#1a1a2e", 
            fg="#ffffff"
        )
        self.result_label.pack(pady=15)

        # --- BUTTONS INTERFACE ---
        btn_frame = tk.Frame(root, bg="#1a1a2e")
        btn_frame.pack(pady=20)

        # Rock Button
        rock_btn = tk.Button(btn_frame, text="✊ Rock", font=("Helvetica", 12, "bold"), bg="#0f3460", fg="#ffffff", activebackground="#e94560", width=12, bd=0, command=lambda: self.play_round("Rock"))
        rock_btn.grid(row=0, column=0, padx=5, pady=5, ipady=10)

        # Paper Button
        paper_btn = tk.Button(btn_frame, text="✋ Paper", font=("Helvetica", 12, "bold"), bg="#0f3460", fg="#ffffff", activebackground="#e94560", width=12, bd=0, command=lambda: self.play_round("Paper"))
        paper_btn.grid(row=0, column=1, padx=5, pady=5, ipady=10)

        # Scissors Button
        scissors_btn = tk.Button(btn_frame, text="✌ Scissors", font=("Helvetica", 12, "bold"), bg="#0f3460", fg="#ffffff", activebackground="#e94560", width=12, bd=0, command=lambda: self.play_round("Scissors"))
        scissors_btn.grid(row=0, column=2, padx=5, pady=5, ipady=10)

        # Reset Game Button
        reset_btn = tk.Button(
            root, text="Reset Game", font=("Helvetica", 10, "bold"), bg="#e94560", fg="#ffffff", bd=0, padx=15, pady=5, command=self.reset_game
        )
        reset_btn.pack(pady=25)

    def play_round(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        self.status_label.config(
            text=f"You chose: {user_choice}   VS   Computer chose: {computer_choice}",
            fg="#ffffff"
        )

        # Game Logic
        if user_choice == computer_choice:
            self.result_label.config(text="It's a Tie! 🤝", fg="#8186a0")
            
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            self.result_label.config(text="You Win This Round! 🎉", fg="#4e9f3d")
            self.user_score += 1
            
        else:
            self.result_label.config(text="Computer Wins This Round! 😢", fg="#ff4b4b")
            self.computer_score += 1

        # Update scoreboard
        self.score_label.config(text=f"You: {self.user_score}   |   Computer: {self.computer_score}")

    def reset_game(self):
        confirm = messagebox.askyesno("Reset Match", "Are you sure you want to clear the scores and start over?")
        if confirm:
            self.user_score = 0
            self.computer_score = 0
            self.score_label.config(text="You: 0   |   Computer: 0")
            self.status_label.config(text="Choose your move to start the game!", fg="#8186a0")
            self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
