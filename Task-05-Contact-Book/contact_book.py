import tkinter as tk
from tkinter import messagebox, ttk

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft Contact Book")
        self.root.geometry("550x650")
        self.root.configure(bg="#1e1e24")
        self.root.resizable(False, False)

        # Contact Storage (Dictionary)
        self.contacts = {}

        # Title
        title_label = tk.Label(
            root, text="CONTACT BOOK", font=("Helvetica", 18, "bold"), bg="#1e1e24", fg="#00adb5"
        )
        title_label.pack(pady=15)

        # --- INPUT FIELDS FRAME ---
        input_frame = tk.Frame(root, bg="#1e1e24")
        input_frame.pack(pady=10, padx=20, fill="x")

        # Labels & Entries Configuration
        fields = [("Name:", "name"), ("Phone:", "phone"), ("Email:", "email"), ("Address:", "address")]
        self.entries = {}

        for i, (label_text, field_name) in enumerate(fields):
            lbl = tk.Label(input_frame, text=label_text, font=("Helvetica", 11), bg="#1e1e24", fg="#ffffff")
            lbl.grid(row=i, column=0, sticky="w", pady=5, padx=5)
            
            entry = tk.Entry(input_frame, font=("Helvetica", 11), bg="#2a2a35", fg="#ffffff", bd=0)
            entry.grid(row=i, column=1, sticky="ew", pady=5, padx=5)
            self.entries[field_name] = entry

        input_frame.columnconfigure(1, weight=1)

        # --- BUTTONS FRAME ---
        btn_frame = tk.Frame(root, bg="#1e1e24")
        btn_frame.pack(pady=10)

        style = ttk.Style()
        style.theme_use("default")
        
        add_btn = tk.Button(btn_frame, text="Add Contact", font=("Helvetica", 10, "bold"), bg="#00adb5", fg="#ffffff", bd=0, padx=15, pady=5, command=self.add_contact)
        add_btn.grid(row=0, column=0, padx=5)

        clear_btn = tk.Button(btn_frame, text="Clear Fields", font=("Helvetica", 10, "bold"), bg="#393e46", fg="#ffffff", bd=0, padx=15, pady=5, command=self.clear_fields)
        clear_btn.grid(row=0, column=1, padx=5)

        delete_btn = tk.Button(btn_frame, text="Delete Selected", font=("Helvetica", 10, "bold"), bg="#ff4141", fg="#ffffff", bd=0, padx=15, pady=5, command=self.delete_contact)
        delete_btn.grid(row=0, column=2, padx=5)

        # --- SEARCH FRAME ---
        search_frame = tk.Frame(root, bg="#1e1e24")
        search_frame.pack(pady=10, padx=20, fill="x")

        search_lbl = tk.Label(search_frame, text="Search (Name/Phone):", font=("Helvetica", 11), bg="#1e1e24", fg="#ffffff")
        search_lbl.grid(row=0, column=0, sticky="w", padx=5)

        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 11), bg="#2a2a35", fg="#ffffff", bd=0)
        self.search_entry.grid(row=0, column=1, sticky="ew", padx=5)
        self.search_entry.bind("<KeyRelease>", self.search_contact)
        
        search_frame.columnconfigure(1, weight=1)

        # --- CONTACT LIST (TREEVIEW) ---
        list_frame = tk.Frame(root, bg="#1e1e24")
        list_frame.pack(pady=15, padx=20, fill="both", expand=True)

        # Style the Treeview table
        style.configure("Treeview", background="#2a2a35", foreground="#ffffff", fieldbackground="#2a2a35", rowheight=25)
        style.map("Treeview", background=[("selected", "#00adb5")])

        self.tree = ttk.Treeview(list_frame, columns=("Name", "Phone", "Email"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone Number")
        self.tree.heading("Email", text="Email")
        
        self.tree.column("Name", width=120)
        self.tree.column("Phone", width=120)
        self.tree.column("Email", width=180)

        # Scrollbar for table
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.tree.bind("<<TreeviewSelect>>", self.display_selected_contact)

    def add_contact(self):
        name = self.entries["name"].get().strip()
        phone = self.entries["phone"].get().strip()
        email = self.entries["email"].get().strip()
        address = self.entries["address"].get().strip()

        if not name or not phone:
            messagebox.showwarning("Warning", "Name and Phone Number are required fields!")
            return

        # Save or update contact information
        self.contacts[phone] = {"name": name, "email": email, "address": address}
        messagebox.showinfo("Success", f"Contact '{name}' saved successfully!")
        self.clear_fields()
        self.update_list()

    def update_list(self, contact_dict=None):
        # Clear existing items in list display
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        display_source = contact_dict if contact_dict is not None else self.contacts
        
        # Repopulate table list
        for phone, info in display_source.items():
            self.tree.insert("", "end", values=(info["name"], phone, info["email"]))

    def display_selected_contact(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
            
        # Extract details from selected row and show in input fields
        values = self.tree.item(selected_item, "values")
        phone = values[1]
        contact = self.contacts.get(phone)
        
        if contact:
            self.clear_fields()
            self.entries["name"].insert(0, contact["name"])
            self.entries["phone"].insert(0, phone)
            self.entries["email"].insert(0, contact["email"])
            self.entries["address"].insert(0, contact["address"])

    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a contact from the list to delete.")
            return

        values = self.tree.item(selected_item, "values")
        phone = values[1]
        name = values[0]
        
        if phone in self.contacts:
            del self.contacts[phone]
            messagebox.showinfo("Deleted", f"Contact '{name}' removed successfully.")
            self.clear_fields()
            self.update_list()

    def search_contact(self, event):
        query = self.search_entry.get().strip().lower()
        if not query:
            self.update_list()
            return

        filtered_contacts = {}
        for phone, info in self.contacts.items():
            if query in info["name"].lower() or query in phone:
                filtered_contacts[phone] = info
                
        self.update_list(filtered_contacts)

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
