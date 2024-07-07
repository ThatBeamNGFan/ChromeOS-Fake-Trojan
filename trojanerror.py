import tkinter as tk
from tkinter import messagebox
import time

def fake_virus():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    messages = [
        "Your system has been infected!",
        "Warning: Virus detected!",
        "Critical Error! Immediate action required!",
        "System failure imminent!",
        "Your files are being deleted...",
        "Haha, just kidding! This is a prank!"
    ]

    for msg in messages:
        messagebox.showwarning("Virus Alert", msg)
        time.sleep(1.5)

    messagebox.showinfo("Relax!", "This was just a prank. Your computer is safe!")

fake_virus()
