import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import ttk
from tkinterweb import HtmlFrame  # Import HtmlFrame from tkinterweb


# Define a class for the ATM application
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.balance = 0
        self.current_user = None

        # Load user data (for simplicity, we'll use a static user)
        self.user_data = {
            "user123": {"pin": "1234", "balance": 1000},
        }

        # Set up the GUI
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)

        # Create login widgets
        self.login_widgets()

    def login_widgets(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.username_label = tk.Label(self.main_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.pin_label = tk.Label(self.main_frame, text="PIN:")
        self.pin_label.grid(row=1, column=0, padx=10, pady=10)
        self.pin_entry = tk.Entry(self.main_frame, show='*')
        self.pin_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.main_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        pin = self.pin_entry.get()

        if username in self.user_data and self.user_data[username]['pin'] == pin:
            self.current_user = username
            self.balance = self.user_data[username]['balance']
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or PIN.")

    def show_main_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(expand=1, fill='both')

        # Create frames for different tabs
        self.create_atm_tab()
        self.create_web_tab()

    def create_atm_tab(self):
        atm_frame = ttk.Frame(self.notebook)
        self.notebook.add(atm_frame, text="ATM")

        tk.Label(atm_frame, text=f"Welcome, {self.current_user}").pack(pady=10)

        tk.Button(atm_frame, text="Check Balance", command=self.check_balance).pack(padx=10, pady=5)
        tk.Button(atm_frame, text="Deposit", command=self.deposit).pack(padx=10, pady=5)
        tk.Button(atm_frame, text="Withdraw", command=self.withdraw).pack(padx=10, pady=5)
        tk.Button(atm_frame, text="Transfer", command=self.transfer).pack(padx=10, pady=5)
        tk.Button(atm_frame, text="Change PIN", command=self.change_pin).pack(padx=10, pady=5)
        tk.Button(atm_frame, text="Logout", command=self.logout).pack(padx=10, pady=10)

    def create_web_tab(self):
        web_frame = ttk.Frame(self.notebook)
        self.notebook.add(web_frame, text="Web Browser")

        # Create an HtmlFrame to display HTML content
        self.web_frame = HtmlFrame(web_frame, horizontal_scrollbar="auto")
        self.web_frame.pack(expand=1, fill='both')

        # Load example content
        self.load_web_content()

    def load_web_content(self):
        # Example HTML content, you can replace this with a URL or more complex HTML
        html_content = """
        <html>
        <body>
        <h1>Welcome to the ATM Web Browser</h1>
        <p>This tab can display HTML content. Replace this with actual web content.</p>
        </body>
        </html>
        """
        self.web_frame.set_content(html_content)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is ${self.balance:.2f}")

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amount and amount > 0:
            self.balance += amount
            self.user_data[self.current_user]['balance'] = self.balance
            messagebox.showinfo("Deposit", f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            messagebox.showwarning("Warning", "Invalid amount.")

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        if amount and 0 < amount <= self.balance:
            self.balance -= amount
            self.user_data[self.current_user]['balance'] = self.balance
            messagebox.showinfo("Withdraw", f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            messagebox.showwarning("Warning", "Insufficient funds.")
        else:
            messagebox.showwarning("Warning", "Invalid amount.")

    def transfer(self):
        amount = simpledialog.askfloat("Transfer", "Enter amount to transfer:")
        if amount and 0 < amount <= self.balance:
            recipient = simpledialog.askstring("Transfer", "Enter recipient username:")
            if recipient in self.user_data:
                self.balance -= amount
                self.user_data[self.current_user]['balance'] = self.balance
                self.user_data[recipient]['balance'] += amount
                messagebox.showinfo("Transfer",
                                    f"Transferred ${amount:.2f} to {recipient}. New balance: ${self.balance:.2f}")
            else:
                messagebox.showwarning("Warning", "Recipient not found.")
        elif amount > self.balance:
            messagebox.showwarning("Warning", "Insufficient funds.")
        else:
            messagebox.showwarning("Warning", "Invalid amount.")

    def change_pin(self):
        new_pin = simpledialog.askstring("Change PIN", "Enter new PIN:")
        if new_pin and len(new_pin) == 4 and new_pin.isdigit():
            self.user_data[self.current_user]['pin'] = new_pin
            messagebox.showinfo("Change PIN", "PIN changed successfully.")
        else:
            messagebox.showwarning("Warning", "Invalid PIN. It must be 4 digits.")

    def logout(self):
        self.current_user = None
        self.balance = 0
        self.login_widgets()


# Create the main application window
root = tk.Tk()
app = ATMApp(root)
root.mainloop()
