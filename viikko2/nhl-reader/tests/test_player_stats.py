import unittest

from player import Player, PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "assists": 10,
                "goals": 5,
                "team": "AAA",
            }),
            Player({
                "name": "Player Two",
                "nationality": "SWE",
                "assists": 4,
                "goals": 8,
                "team": "AAA",
            }),
            Player({
                "name": "Player Three",
                "nationality": "USA",
                "assists": 20,
                "goals": 10,
                "team": "BBB",
            }),
            Player({
                "name": "Player Four",
                "nationality": "FIN",
                "assists": 12,
                "goals": 8,
                "team": "BBB",
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_team_are_sorted_by_points(self):
        players = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(
            [player.name for player in players],
            ["Player One", "Player Two"],
        )

    def test_top_scorers_by_team_returns_empty_list_when_team_not_found(self):
        self.assertEqual(self.stats.top_scorers_by_team("XXX"), [])

    def test_top_scorers_by_nationality_are_sorted_by_points(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in players],
            ["Player Four", "Player One"],
        )

    def test_top_scorers_by_nationality_returns_empty_list_when_not_found(self):
        self.assertEqual(self.stats.top_scorers_by_nationality("XXX"), [])


if __name__ == "__main__":
    unittest.main()
