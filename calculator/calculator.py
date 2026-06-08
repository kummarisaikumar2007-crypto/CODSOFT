import tkinter as tk
from tkinter import messagebox

class ProfessionalCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft Advanced Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#17171c")
        self.root.resizable(False, False)

        self.expression = ""

        # Display Screen
        self.display = tk.Entry(
            root, 
            font=("Helvetica", 32), 
            bg="#17171c", 
            fg="#ffffff", 
            bd=0, 
            justify="right"
        )
        self.display.pack(expand=True, fill="both", padx=20, pady=20)
        self.display.insert(0, "0")

        # Button Layout Configuration
        self.buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '+/-', '=']
        ]

        self.create_buttons()

    def create_buttons(self):
        button_container = tk.Frame(self.root, bg="#17171c")
        button_container.pack(expand=True, fill="both")

        for row_idx, row in enumerate(self.buttons):
            button_container.rowconfigure(row_idx, weight=1)
            for col_idx, text in enumerate(row):
                button_container.columnconfigure(col_idx, weight=1)
                
                # Dynamic styling based on button type
                if text in ['/', '*', '-', '+', '=']:
                    bg_color = "#ff9f0a"  # Orange for operators
                    fg_color = "#ffffff"
                elif text in ['C', '(', ')', '+/-']:
                    bg_color = "#a5a5a5"  # Light gray for top controls
                    fg_color = "#000000"
                else:
                    bg_color = "#333333"  # Dark gray for numbers
                    fg_color = "#ffffff"

                btn = tk.Button(
                    button_container, 
                    text=text, 
                    font=("Helvetica", 20, "bold"),
                    bg=bg_color, 
                    fg=fg_color, 
                    bd=0,
                    activebackground="#555555",
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_display("0")
        
        elif char == '=':
            try:
                # Safely evaluate the math string expression
                result = str(eval(self.expression))
                self.update_display(result)
                self.expression = result  # Allow continuing calculations
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.clear_screen()
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.clear_screen()
                
        elif char == '+/-':
            try:
                if self.expression:
                    if self.expression.startswith('-'):
                        self.expression = self.expression[1:]
                    else:
                        self.expression = '-' + self.expression
                    self.update_display(self.expression)
            except Exception:
                pass
                
        else:
            # Prevent leading zeros from stacking
            if self.expression == "" and char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.expression = char
            else:
                self.expression += str(char)
            self.update_display(self.expression)

    def update_display(self, text):
        self.display.delete(0, tk.END)
        self.display.insert(0, text)

    def clear_screen(self):
        self.expression = ""
        self.update_display("0")

# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ProfessionalCalculator(root)
    root.mainloop()
