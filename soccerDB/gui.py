import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

# Create the GUI root
root = tk.Tk()
root.title("International Soccer Results Database App")
root.iconbitmap("images/football.ico")
root.geometry("1000x461")

# Create tkinter variables
hometeam = tk.StringVar()
awayteam = tk.StringVar()

# Add background image
background_image = ImageTk.PhotoImage(Image.open("images/soccer_bg.jpg"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create font(s) for the GUI
label_font = Font(family="Arial", size=14)

# Create labels
label_hometeam = tk.Label(
    root, text="Choose the home team:", font=label_font, fg="white", bg="#333"
)
label_awayteam = tk.Label(
    root, text="Choose the away team:", font=label_font, fg="white", bg="#333"
)

# Create drop down menus
dropdown_hometeam = tk.OptionMenu(root, hometeam, "Sweden", "Denmark")

# Place labels
label_hometeam.grid(row=0, column=0, padx=(50, 0), pady=(10, 0))
label_awayteam.grid(row=1, column=0, padx=(50, 0), pady=(10, 0))

root.mainloop()
