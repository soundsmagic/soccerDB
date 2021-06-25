import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
import DBhandling


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("International Soccer Results Database App")
        master.geometry("1000x461")
        master.iconbitmap("images/football.ico")
        self.label_font = Font(family="Arial", size=14)
        self.create_background()
        self.create_labels()

    def create_background(self):
        self.background_image = ImageTk.PhotoImage(Image.open("images/soccer_bg.jpg"))
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_labels(self):
        self.label_hometeam = tk.Label(
            self.master,
            text="Choose the home team:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_awayteam = tk.Label(
            self.master,
            text="Choose the away team:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_hometeam.grid(row=0, column=0, padx=(50, 0), pady=(10, 0))
        self.label_awayteam.grid(row=1, column=0, padx=(50, 0), pady=(10, 0))

    def create_dropdowns(self):
        self.hometeam = tk.StringVar()
        self.dropdown_hometeam = tk.OptionMenu(
            self.master, self.hometeam, "Sweden", "Denmark"
        )
        self.awayteam = tk.StringVar()
