import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
from PIL import ImageTk, Image
import DBhandling


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.dbObject = DBhandling.Database()
        self.countryList = self.dbObject.FetchCountries()
        master.title("International Soccer Results Database App")
        master.geometry("1000x461")
        master.iconbitmap("images/football.ico")
        self.label_font = Font(family="Arial", size=14)
        self.create_background()
        self.create_static_labels()
        self.create_hidden_result_labels()
        self.create_dropdowns()
        self.create_buttons()

    def MakeLabel(self, textInput):
        return tk.Label(
            self.master,
            text=textInput,
            font=self.label_font,
            fg="white",
            bg="#333",
        )

    def create_background(self):
        self.background_image = ImageTk.PhotoImage(Image.open("images/soccer_bg.jpg"))
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_dropdowns(self):
        self.firstteam = tk.StringVar()
        self.dropdown_firstteam = ttk.Combobox(self.master, values=self.countryList)
        self.dropdown_firstteam.grid(row=0, column=1, padx=(50, 0), pady=(10, 0))
        self.dropdown_firstteam.current(1)
        self.secondteam = tk.StringVar()
        self.dropdown_secondteam = ttk.Combobox(self.master, values=self.countryList)
        self.dropdown_secondteam.grid(row=1, column=1, padx=(50, 0), pady=(10, 0))
        self.dropdown_secondteam.current(1)

    def create_static_labels(self):
        self.label_chooseFirstTeam = self.MakeLabel("Choose the first team:")
        self.label_chooseFirstTeam.grid(
            row=0, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
        )
        self.label_chooseSecondTeam = self.MakeLabel("Choose the second team:")
        self.label_chooseSecondTeam.grid(
            row=1, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
        )

    def create_hidden_result_labels(self):
        self.label_chosenTeams = self.MakeLabel("Chosen teams:")
        self.label_matchesPlayed = self.MakeLabel("Matches played:")
        self.label_wins = self.MakeLabel("Wins:")
        self.label_ties = self.MakeLabel("Tied matches:")
        self.label_homeWins = self.MakeLabel("Home wins:")
        self.label_scoredGoals = self.MakeLabel("Scored goals:")
        self.label_neutralMatches = self.MakeLabel("Matches on neutral ground:")
        self.label_earliestMatch = self.MakeLabel("Earliest match:")
        self.label_chosenFirstTeam = self.MakeLabel("")
        self.label_chosenSecondTeam = self.MakeLabel("")
        self.label_matchesPlayedResult = self.MakeLabel("")
        self.label_firstTeamWins = self.MakeLabel("")
        self.label_secondTeamWins = self.MakeLabel("")
        self.label_tiedMatches = self.MakeLabel("")
        self.label_homeWinsFirstTeam = self.MakeLabel("")
        self.label_homeWinsSecondTeam = self.MakeLabel("")
        self.label_scoredGoalsFirstTeam = self.MakeLabel("")
        self.label_scoredGoalsSecondTeam = self.MakeLabel("")
        self.label_neutralMatchesPlayed = self.MakeLabel("")
        self.label_earliestMatchResult = self.MakeLabel("")

    def generate_results(self):
        if self.dropdown_firstteam.get() == self.dropdown_secondteam.get():
            tk.messagebox.showerror(
                title="Error: Duplicate teams chosen",
                message="Please choose two different teams.",
            )
        elif (
            self.dropdown_firstteam.get() in self.countryList
            and self.dropdown_secondteam.get() in self.countryList
        ):
            self.label_chosenTeams.grid(
                row=2, column=0, padx=(50, 0), pady=(40, 0), sticky="E"
            )
            self.label_matchesPlayed.grid(
                row=3, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
            )
            self.label_wins.grid(
                row=4, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
            )
            self.label_ties.grid(
                row=5, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
            )
            self.label_homeWins.grid(
                row=6, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
            )
            self.label_scoredGoals.grid(
                row=7, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
            )
            self.label_neutralMatches.grid(
                row=8, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
            )
            self.label_earliestMatch.grid(
                row=9, column=0, padx=(50, 0), pady=(10, 0), sticky="E"
            )
            self.label_chosenFirstTeam["text"] = self.dropdown_firstteam.get()
            self.label_chosenFirstTeam.grid(row=2, column=1, padx=(50, 0), pady=(40, 0))
            self.label_chosenSecondTeam["text"] = self.dropdown_secondteam.get()
            self.label_chosenSecondTeam.grid(
                row=2, column=2, padx=(50, 0), pady=(40, 0)
            )
            self.label_matchesPlayedResult["text"] = self.dbObject.MatchesPlayed(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            )
            self.label_matchesPlayedResult.grid(
                row=3, column=1, columnspan=2, padx=(50, 0), pady=(10, 0)
            )
            self.label_firstTeamWins["text"] = self.dbObject.Wins(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            )
            self.label_firstTeamWins.grid(row=4, column=1, padx=(50, 0), pady=(10, 0))
            self.label_secondTeamWins["text"] = self.dbObject.Wins(
                self.dropdown_secondteam.get(), self.dropdown_firstteam.get()
            )
            self.label_secondTeamWins.grid(row=4, column=2, padx=(50, 0), pady=(10, 0))
            self.label_tiedMatches["text"] = self.dbObject.Ties(
                self.dropdown_secondteam.get(), self.dropdown_firstteam.get()
            )
            self.label_tiedMatches.grid(
                row=5, column=1, columnspan=2, padx=(50, 0), pady=(10, 0)
            )
            self.label_homeWinsFirstTeam["text"] = self.dbObject.HomeWins(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            )
            self.label_homeWinsFirstTeam.grid(
                row=6, column=1, padx=(50, 0), pady=(10, 0)
            )
            self.label_homeWinsSecondTeam["text"] = self.dbObject.HomeWins(
                self.dropdown_secondteam.get(), self.dropdown_firstteam.get()
            )
            self.label_homeWinsSecondTeam.grid(
                row=6, column=2, padx=(50, 0), pady=(10, 0)
            )
            self.label_scoredGoalsFirstTeam["text"] = self.dbObject.ScoredGoals(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            )
            self.label_scoredGoalsFirstTeam.grid(
                row=7, column=1, padx=(50, 0), pady=(10, 0)
            )
            self.label_scoredGoalsSecondTeam["text"] = self.dbObject.ScoredGoals(
                self.dropdown_secondteam.get(), self.dropdown_firstteam.get()
            )
            self.label_scoredGoalsSecondTeam.grid(
                row=7, column=2, padx=(50, 0), pady=(10, 0)
            )
            self.label_neutralMatchesPlayed["text"] = self.dbObject.NeutralMatches(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            )
            self.label_neutralMatchesPlayed.grid(
                row=8, column=1, columnspan=2, padx=(50, 0), pady=(10, 0)
            )
            self.label_earliestMatchResult["text"] = self.dbObject.EarliestMatch(
                self.dropdown_firstteam.get(), self.dropdown_secondteam.get()
            )
            self.label_earliestMatchResult.grid(
                row=9, column=1, columnspan=2, padx=(50, 0), pady=(10, 0)
            )
        else:
            tk.messagebox.showerror(
                title="Error: One or more teams not found",
                message="One or more teams was not found in the database.",
            )

    def create_buttons(self):
        self.getFactsButton = tk.Button(
            self.master, text="Get facts", command=self.generate_results
        )
        self.getFactsButton.grid(
            row=0, rowspan=2, column=2, padx=(20, 0), pady=(10, 0), ipadx=25, ipady=5
        )
