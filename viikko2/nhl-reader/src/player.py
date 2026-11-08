import requests


class Player:  # pylint: disable=too-few-public-methods
    def __init__(self, player_data):
        self.name = player_data['name']
        self.nation = player_data['nationality']
        self.assist = player_data['assists']
        self.goals = player_data['goals']
        self.team = player_data['team']
        self.total = self.assist + self.goals

    def __str__(self):
        return (
            f"{self.name:20} team {self.team:20} goals "
            f"{self.goals} + {self.assist} = {self.total}"
        )


class PlayerReader:  # pylint: disable=too-few-public-methods
    def __init__(self, url):
        self.url = url
        response = requests.get(url, timeout=10).json()
        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

    def get_players(self):
        return self.players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä.
        """


    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self.players:
            if player.nation == nationality:
                players.append(player)

        return sorted(players, key=lambda player: player.total, reverse=True)

    def top_scorers_by_team(self, team):
        players = []

        for player in self.players:
            if player.team == team:
                players.append(player)

        return sorted(players, key=lambda player: player.total, reverse=True)
