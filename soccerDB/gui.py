import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import ImageTk, Image
import DBhandling


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.dbObject = DBhandling.Database()
        master.title("International Soccer Results Database App")
        master.geometry("1000x461")
        master.iconbitmap("images/football.ico")
        self.label_font = Font(family="Arial", size=14)
        self.create_background()
        self.create_labels()
        self.create_dropdowns()
        self.create_buttons()

    def create_background(self):
        self.background_image = ImageTk.PhotoImage(Image.open("images/soccer_bg.jpg"))
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_labels(self):
        self.label_chooseFirstTeam = tk.Label(
            self.master,
            text="Choose the first team:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_chooseSecondTeam = tk.Label(
            self.master,
            text="Choose the second team:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_chosenTeams = tk.Label(
            self.master,
            text="Chosen teams:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_matchesPlayed = tk.Label(
            self.master,
            text="Matches played:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_wins = tk.Label(
            self.master,
            text="Wins:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_ties = tk.Label(
            self.master,
            text="Tied matches:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_homeWins = tk.Label(
            self.master,
            text="Home wins:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_scoredGoals = tk.Label(
            self.master,
            text="Scored goals:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_neutralMatches = tk.Label(
            self.master,
            text="Matches on neutral ground:",
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_chooseFirstTeam.grid(row=0, column=0, padx=(50, 0), pady=(10, 0))
        self.label_chooseSecondTeam.grid(row=1, column=0, padx=(50, 0), pady=(10, 0))
        self.label_chosenTeams.grid(row=2, column=0, padx=(50, 0), pady=(40, 0))
        self.label_matchesPlayed.grid(row=3, column=0, padx=(50, 0), pady=(10, 0))
        self.label_wins.grid(row=4, column=0, padx=(50, 0), pady=(10, 0))
        self.label_ties.grid(row=5, column=0, padx=(50, 0), pady=(10, 0))
        self.label_homeWins.grid(row=6, column=0, padx=(50, 0), pady=(10, 0))
        self.label_scoredGoals.grid(row=7, column=0, padx=(50, 0), pady=(10, 0))
        self.label_neutralMatches.grid(row=8, column=0, padx=(50, 0), pady=(10, 0))

    def create_dropdowns(self):
        self.firstteam = tk.StringVar()
        self.dropdown_firstteam = ttk.Combobox(
            self.master, values=self.dbObject.FetchCountries()
        )
        self.dropdown_firstteam.grid(row=0, column=1, padx=(50, 0), pady=(10, 0))
        self.dropdown_firstteam.current(1)
        self.secondteam = tk.StringVar()
        self.dropdown_secondteam = ttk.Combobox(
            self.master, values=self.dbObject.FetchCountries()
        )
        self.dropdown_secondteam.grid(row=1, column=1, padx=(50, 0), pady=(10, 0))
        self.dropdown_secondteam.current(1)

    def create_buttons(self):
        self.getFactsButton = tk.Button(
            self.master, text="Get facts", command=self.getFacts
        )
        self.getFactsButton.grid(
            row=0, rowspan=2, column=2, padx=(20, 0), pady=(10, 0), ipadx=25, ipady=5
        )

    def getFacts(self):
        self.label_chosenFirstTeam = tk.Label(
            self.master,
            text=self.dropdown_firstteam.get(),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_chosenFirstTeam.grid(row=2, column=1, padx=(50, 0), pady=(40, 0))
        self.label_chosenSecondTeam = tk.Label(
            self.master,
            text=self.dropdown_secondteam.get(),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_chosenSecondTeam.grid(row=2, column=2, padx=(50, 0), pady=(40, 0))
        self.label_matchesPlayedResult = tk.Label(
            self.master,
            text=self.dbObject.MatchesPlayed(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_matchesPlayedResult.grid(
            row=3, column=1, columnspan=2, padx=(50, 0), pady=(10, 0)
        )
        self.label_firstTeamWins = tk.Label(
            self.master,
            text=self.dbObject.Wins(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_firstTeamWins.grid(row=4, column=1, padx=(50, 0), pady=(10, 0))
        self.label_secondTeamWins = tk.Label(
            self.master,
            text=self.dbObject.Wins(
                self.dropdown_secondteam.get(), self.dropdown_firstteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_secondTeamWins.grid(row=4, column=2, padx=(50, 0), pady=(10, 0))
        self.label_tiedMatches = tk.Label(
            self.master,
            text=self.dbObject.Ties(
                self.dropdown_secondteam.get(), self.dropdown_firstteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_tiedMatches.grid(
            row=5, column=1, columnspan=2, padx=(50, 0), pady=(10, 0)
        )
        self.label_homeWinsFirstTeam = tk.Label(
            self.master,
            text=self.dbObject.HomeWins(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_homeWinsFirstTeam.grid(row=6, column=1, padx=(50, 0), pady=(10, 0))
        self.label_homeWinsSecondTeam = tk.Label(
            self.master,
            text=self.dbObject.HomeWins(
                self.dropdown_secondteam.get(), self.dropdown_firstteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_homeWinsSecondTeam.grid(row=6, column=2, padx=(50, 0), pady=(10, 0))
        self.label_scoredGoalsFirstTeam = tk.Label(
            self.master,
            text=self.dbObject.ScoredGoals(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_scoredGoalsFirstTeam.grid(
            row=7, column=1, padx=(50, 0), pady=(10, 0)
        )
        self.label_scoredGoalsSecondTeam = tk.Label(
            self.master,
            text=self.dbObject.ScoredGoals(
                self.dropdown_secondteam.get(), self.dropdown_firstteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_scoredGoalsSecondTeam.grid(
            row=7, column=2, padx=(50, 0), pady=(10, 0)
        )
        self.label_neutralMatchesPlayed = tk.Label(
            self.master,
            text=self.dbObject.NeutralMatches(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            ),
            font=self.label_font,
            fg="white",
            bg="#333",
        )
        self.label_neutralMatchesPlayed.grid(
            row=8, column=1, columnspan=2, padx=(50, 0), pady=(10, 0)
        )
