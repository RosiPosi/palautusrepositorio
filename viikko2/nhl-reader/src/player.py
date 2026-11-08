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
    
        
