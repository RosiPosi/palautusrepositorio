import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nation = dict['nationality']
        self.assist = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.total = self.assist + self.goals
    
    def __str__(self):
        return f"{self.name:20} team {self.team:20} goals {self.goals} + {self.assist} = {self.total}"
    
class PlayerReader:
    def __init__(self, url):
        self.url = url
        response = requests.get(url).json()
        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

    def get_players(self):
        return self.players
    
class PlayerStats:
    def top_scorers_by_nationality(self, dict):
        pass
        

