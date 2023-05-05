import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class LoginPage(tk.Frame):
    def __init__(self, master, on_login):
        super().__init__(master)
        self.on_login = on_login

        tk.Label(self, text="Username:").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self, text="Password:").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

      
        if username == "amalks" and password == "password":
            self.on_login()
        else:
            messagebox.showerror("Error", "Invalid username or password")

class ThanksPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Thanks for logging in AMAL K S  !").pack()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Example")
        self.geometry("300x200")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.login_page = LoginPage(self.notebook, self.show_thanks_page)
        self.notebook.add(self.login_page, text="Login")

    def show_thanks_page(self):
        self.thanks_page = ThanksPage(self.notebook)
        self.notebook.add(self.thanks_page, text="Thanks!")
        self.notebook.select(self.thanks_page)

app = Application()
app.mainloop()



