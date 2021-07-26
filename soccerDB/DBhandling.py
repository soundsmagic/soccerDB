import pyodbc
import datetime


class Database:
    def __init__(self):
        self.conn_str = (
            r"Driver={SQL Server Native Client 11.0};"
            r"Server=(localdb)\MSSQLLocalDB;"
            r"Database=C:\USERS\JOHN-\ONEDRIVE\DOKUMENT\SQL ASSIGNMENT.mdf;"
            r"Trusted_Connection=yes;"
        )
        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()

    def FetchCountries(self):
        self.cursor.execute("SELECT DISTINCT [Home Team] FROM SoccerResults")
        return sorted([i[0] for i in self.cursor.fetchall()])

    def MatchesPlayed(self, teamOne, teamTwo):
        self.cursor.execute(
            f"SELECT COUNT(CASE WHEN ([Home Team] = '{teamOne}' AND [Away Team] = '{teamTwo}') OR ([Home Team] = '{teamTwo}' AND [Away Team] = '{teamOne}') THEN 1 END) AS Matches FROM SoccerResults"
        )
        return self.cursor.fetchone()[0]

    def Wins(self, teamOne, teamTwo):
        self.cursor.execute(
            f"SELECT COUNT(CASE WHEN ([Home Team] = '{teamOne}' AND [Away Team] = '{teamTwo}' AND [Home Score] > [Away Score]) OR ([Home Team] = '{teamTwo}' AND [Away Team] = '{teamOne}' AND [Away Score] > [Home Score]) THEN 1 END) FROM SoccerResults"
        )
        return self.cursor.fetchone()[0]

    def Ties(self, teamOne, teamTwo):
        self.cursor.execute(
            f"SELECT COUNT(CASE WHEN ([Home Team] = '{teamOne}' AND [Away Team] = '{teamTwo}' AND [Home Score] = [Away Score]) OR ([Home Team] = '{teamTwo}' AND [Away Team] = '{teamOne}' AND [Away Score] = [Home Score]) THEN 1 END) FROM SoccerResults"
        )
        return self.cursor.fetchone()[0]

    def HomeWins(self, teamOne, teamTwo):
        self.cursor.execute(
            f"SELECT COUNT(CASE WHEN ([Home Team] = '{teamOne}' AND [Away Team] = '{teamTwo}' AND [Home Score] > [Away Score])THEN 1 END) FROM SoccerResults"
        )
        return self.cursor.fetchone()[0]

    def ScoredGoals(self, teamOne, teamTwo):
        self.cursor.execute(
            f"SELECT SUM(CASE WHEN ([Home Team] = '{teamOne}' AND [Away Team] = '{teamTwo}') THEN [Home Score] ELSE 0 END + CASE WHEN ([Home Team] = '{teamTwo}' AND [Away Team] = '{teamOne}') THEN [Away Score] ELSE 0 END) FROM SoccerResults"
        )
        return self.cursor.fetchone()[0]

    def NeutralMatches(self, teamOne, teamTwo):
        self.cursor.execute(
            f"SELECT COUNT(CASE WHEN ([Home Team] = '{teamOne}' AND [Away Team] = '{teamTwo}' AND [NeutralArena] = 1) OR ([Home Team] = '{teamTwo}' AND [Away Team] = '{teamOne}' AND [NeutralArena] = 1) THEN 1 END) FROM SoccerResults"
        )
        return self.cursor.fetchone()[0]

    def EarliestMatch(self, teamOne, teamTwo):
        self.cursor.execute(
            f"SELECT TOP 1 [Date], [Tournament Name] FROM SoccerResults WHERE [Home Team] = '{teamOne}' AND [Away Team] = '{teamTwo}' OR ([Home Team] = '{teamTwo}' AND [Away Team] = '{teamOne}') ORDER BY [Date]"
        )
        result = self.cursor.fetchone()
        return f"{result[0].strftime('%Y-%m-%d')} ({result[1]})"
