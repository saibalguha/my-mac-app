import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Success", "Hello! This Python app was compiled on a macOS Cloud Runner!")

root = tk.Tk()
root.title("My First macOS Python App")
root.geometry("350x180")

label = tk.Label(root, text="Welcome to my macOS App!", font=("Helvetica", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_click, width=15)
button.pack(pady=10)

root.mainloop()
