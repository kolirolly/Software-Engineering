"""
Cricket Team Management System
Name: Swiften Khan (2418)
"""

class Player:
    def __init__(self, name, role, batting_style="Right-handed", bowling_style=None):
        self.name = name
        self.role = role  # Batsman, Bowler, All-rounder, Wicketkeeper
        self.batting_style = batting_style
        self.bowling_style = bowling_style
        self.jersey_number = None
        self.is_captain = False
        self.stats = {"matches": 0, "runs": 0, "wickets": 0}
    
    def assign_jersey(self, number):
        self.jersey_number = number
        
    def make_captain(self):
        self.is_captain = True
        
    def update_stats(self, matches=0, runs=0, wickets=0):
        self.stats["matches"] += matches
        self.stats["runs"] += runs
        self.stats["wickets"] += wickets
    
    def __str__(self):
        captain_tag = " (Captain)" if self.is_captain else ""
        jersey = f" #{self.jersey_number}" if self.jersey_number else ""
        return f"{self.name}{jersey} - {self.role}{captain_tag}"


class Team:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.players = []
        self.coach = None
        self.captain = None
        self.record = {"played": 0, "won": 0, "lost": 0, "draw": 0}
    
    def add_player(self, player, jersey_number=None, is_captain=False):
        if len(self.players) >= 15:
            print(f"Team {self.name} already has maximum players (15)!")
            return False
        
        if jersey_number:
            # Check if jersey number is already assigned
            for p in self.players:
                if p.jersey_number == jersey_number:
                    print(f"Jersey #{jersey_number} already assigned to {p.name}!")
                    return False
            player.assign_jersey(jersey_number)
        
        if is_captain:
            if self.captain:
                self.captain.is_captain = False
            player.make_captain()
            self.captain = player
            
        self.players.append(player)
        return True
    
    def set_coach(self, name):
        self.coach = name
    
    def show_team(self):
        print(f"\n==== {self.name} ({self.country}) ====")
        if self.coach:
            print(f"Coach: {self.coach}")
        print(f"Record: W{self.record['won']} L{self.record['lost']} D{self.record['draw']} (Played: {self.record['played']})")
        
        print("\nSquad:")
        for player in self.players:
            print(f"  {player}")
            
        if self.captain:
            print(f"\nCaptain: {self.captain.name}")
    
    def update_record(self, result):
        self.record["played"] += 1
        if result == "win":
            self.record["won"] += 1
        elif result == "loss":
            self.record["lost"] += 1
        else:
            self.record["draw"] += 1
    
    def get_playing_xi(self):
        """Returns the first 11 players as the playing XI"""
        return self.players[:11] if len(self.players) >= 11 else self.players


class Match:
    def __init__(self, team1, team2, venue, match_type="ODI"):
        self.team1 = team1
        self.team2 = team2
        self.venue = venue
        self.match_type = match_type
        self.team1_score = {"runs": 0, "wickets": 0}
        self.team2_score = {"runs": 0, "wickets": 0}
        self.result = None
    
    def start_match(self, toss_winner, decision):
        print(f"\n----- Match: {self.team1.name} vs {self.team2.name} -----")
        print(f"Venue: {self.venue}")
        print(f"Format: {self.match_type}")
        print(f"Toss: {toss_winner} won and chose to {decision} first")
    
    def update_score(self, team, runs, wickets):
        if team == self.team1:
            self.team1_score["runs"] = runs
            self.team1_score["wickets"] = wickets
        else:
            self.team2_score["runs"] = runs
            self.team2_score["wickets"] = wickets
        
        print(f"\nCurrent Score:")
        print(f"{self.team1.name}: {self.team1_score['runs']}/{self.team1_score['wickets']}")
        print(f"{self.team2.name}: {self.team2_score['runs']}/{self.team2_score['wickets']}")
    
    def end_match(self):
        if self.team1_score["runs"] > self.team2_score["runs"]:
            self.result = f"{self.team1.name} won by {self.team1_score['runs'] - self.team2_score['runs']} runs"
            self.team1.update_record("win")
            self.team2.update_record("loss")
        elif self.team2_score["runs"] > self.team1_score["runs"]:
            self.result = f"{self.team2.name} won by {self.team2_score['runs'] - self.team1_score['runs']} runs"
            self.team2.update_record("win")
            self.team1.update_record("loss")
        else:
            self.result = "Match ended in a draw"
            self.team1.update_record("draw")
            self.team2.update_record("draw")
        
        print(f"\nResult: {self.result}")


# Example usage
if __name__ == "__main__":
    # Create Teams
    india = Team("India", "India")
    australia = Team("Australia", "Australia")
    
    # Set coaches
    india.set_coach("Rahul Dravid")
    australia.set_coach("Andrew McDonald")
    
    # Create and add players for India
    rohit = Player("Rohit Sharma", "Batsman")
    virat = Player("Virat Kohli", "Batsman")
    bumrah = Player("Jasprit Bumrah", "Bowler", bowling_style="Fast")
    pant = Player("Rishabh Pant", "Wicketkeeper", batting_style="Left-handed")
    hardik = Player("Hardik Pandya", "All-rounder", bowling_style="Medium Fast")
    
    india.add_player(rohit, 45, is_captain=True)
    india.add_player(virat, 18)
    india.add_player(bumrah, 93)
    india.add_player(pant, 17)
    india.add_player(hardik, 33)
    india.add_player(Player("Ravindra Jadeja", "All-rounder", "Left-handed", "Spin"), 8)
    india.add_player(Player("KL Rahul", "Batsman"), 1)
    india.add_player(Player("Mohammed Shami", "Bowler", bowling_style="Fast"), 11)
    india.add_player(Player("Yuzvendra Chahal", "Bowler", bowling_style="Spin"), 3)
    india.add_player(Player("Shubman Gill", "Batsman"), 77)
    india.add_player(Player("Mohammed Siraj", "Bowler", bowling_style="Fast"), 13)
    
    # Add players for Australia
    smith = Player("Steve Smith", "Batsman")
    cummins = Player("Pat Cummins", "Bowler", bowling_style="Fast")
    
    australia.add_player(smith, 49)
    australia.add_player(cummins, 30, is_captain=True)
    australia.add_player(Player("David Warner", "Batsman", "Left-handed"), 31)
    australia.add_player(Player("Mitchell Starc", "Bowler", bowling_style="Fast Left-arm"), 56)
    australia.add_player(Player("Glenn Maxwell", "All-rounder", bowling_style="Off Spin"), 32)
    australia.add_player(Player("Alex Carey", "Wicketkeeper", "Left-handed"), 4)
    australia.add_player(Player("Mitchell Marsh", "All-rounder", bowling_style="Medium"), 8)
    australia.add_player(Player("Nathan Lyon", "Bowler", bowling_style="Off Spin"), 67)
    australia.add_player(Player("Marnus Labuschagne", "Batsman"), 33)
    australia.add_player(Player("Josh Hazlewood", "Bowler", bowling_style="Fast Medium"), 38)
    australia.add_player(Player("Travis Head", "Batsman", "Left-handed"), 62)
    
    # Display teams
    india.show_team()
    australia.show_team()
    
    # Create and simulate a match
    match = Match(india, australia, "Sydney Cricket Ground", "ODI")
    match.start_match("India", "bat")
    
    # Update scores as the match progresses
    match.update_score(india, 287, 6)
    match.update_score(australia, 162, 4)
    match.update_score(australia, 270, 9)
    
    # End the match
    match.end_match()