import tkinter as tk
from tkinter import messagebox
import random
import string

class AdvancedPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft Password Generator")
        self.root.geometry("450x550")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        # Title Label
        title_label = tk.Label(
            root, 
            text="PASSWORD GENERATOR", 
            font=("Helvetica", 18, "bold"), 
            bg="#121212", 
            fg="#00adb5"
        )
        title_label.pack(pady=25)

        # Input Frame (Length Selection)
        input_frame = tk.Frame(root, bg="#121212")
        input_frame.pack(pady=10)

        length_label = tk.Label(
            input_frame, 
            text="Password Length:", 
            font=("Helvetica", 12), 
            bg="#121212", 
            fg="#ffffff"
        )
        length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.length_entry = tk.Entry(
            input_frame, 
            font=("Helvetica", 12), 
            width=8, 
            bg="#222831", 
            fg="#ffffff", 
            bd=0, 
            justify="center"
        )
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)
        self.length_entry.insert(0, "12")  # Default length

        # Settings Frame (Complexity Checkboxes)
        settings_frame = tk.LabelFrame(
            root, 
            text=" Complexity Settings ", 
            font=("Helvetica", 11, "bold"), 
            bg="#121212", 
            fg="#00adb5", 
            bd=1, 
            relief="solid",
            padx=15,
            pady=15
        )
        settings_frame.pack(pady=20, padx=30, fill="both")

        # Variables for Checkboxes
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        # Checkbox widgets
        cb_upper = tk.Checkbutton(settings_frame, text="Include Uppercase Letters (A-Z)", variable=self.use_uppercase, bg="#121212", fg="#ffffff", selectcolor="#222831", activebackground="#121212", activeforeground="#ffffff", font=("Helvetica", 10))
        cb_upper.pack(anchor="w", pady=5)

        cb_lower = tk.Checkbutton(settings_frame, text="Include Lowercase Letters (a-z)", variable=self.use_lowercase, bg="#121212", fg="#ffffff", selectcolor="#222831", activebackground="#121212", activeforeground="#ffffff", font=("Helvetica", 10))
        cb_lower.pack(anchor="w", pady=5)

        cb_num = tk.Checkbutton(settings_frame, text="Include Numbers (0-9)", variable=self.use_numbers, bg="#121212", fg="#ffffff", selectcolor="#222831", activebackground="#121212", activeforeground="#ffffff", font=("Helvetica", 10))
        cb_num.pack(anchor="w", pady=5)

        cb_sym = tk.Checkbutton(settings_frame, text="Include Symbols (!@#$%^&*)", variable=self.use_symbols, bg="#121212", fg="#ffffff", selectcolor="#222831", activebackground="#121212", activeforeground="#ffffff", font=("Helvetica", 10))
        cb_sym.pack(anchor="w", pady=5)

        # Generate Button
        gen_button = tk.Button(
            root, 
            text="Generate Password", 
            font=("Helvetica", 12, "bold"), 
            bg="#00adb5", 
            fg="#ffffff", 
            activebackground="#393e46", 
            activeforeground="#00adb5",
            bd=0, 
            padx=20, 
            pady=8,
            command=self.generate_password
        )
        gen_button.pack(pady=15)

        # Output Box Display
        self.result_entry = tk.Entry(
            root, 
            font=("Helvetica", 14), 
            width=30, 
            bg="#222831", 
            fg="#eeeeee", 
            bd=0, 
            justify="center"
        )
        self.result_entry.pack(pady=15, ipady=8)

        # Copy Button
        copy_button = tk.Button(
            root, 
            text="Copy to Clipboard", 
            font=("Helvetica", 10, "bold"), 
            bg="#393e46", 
            fg="#eeeeee", 
            activebackground="#222831",
            bd=0, 
            padx=10, 
            pady=5,
            command=self.copy_to_clipboard
        )
        copy_button.pack(pady=5)

    def generate_password(self):
        # 1. Get and check the chosen length
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for length.")
            return

        # 2. Build the character pool based on complexity settings
        char_pool = ""
        if self.use_uppercase.get():
            char_pool += string.ascii_uppercase
        if self.use_lowercase.get():
            char_pool += string.ascii_lowercase
        if self.use_numbers.get():
            char_pool += string.digits
        if self.use_symbols.get():
            char_pool += string.punctuation

        # 3. Check if at least one checkbox is selected
        if not char_pool:
            messagebox.showerror("Error", "You must select at least one character type option!")
            return

        # 4. Generate random character choices matching length
        generated_password = "".join(random.choice(char_pool) for _ in range(length))

        # 5. Clear old result text and place the new password inside the display
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, generated_password)

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard successfully!")
        else:
            messagebox.showwarning("Warning", "Generate a password first before copying.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedPasswordGenerator(root)
    root.mainloop()
