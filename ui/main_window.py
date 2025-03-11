# jarvis/ui/main_window.py
# Main GUI window
import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jarvis UI")
