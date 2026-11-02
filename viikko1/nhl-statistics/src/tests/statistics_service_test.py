import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_player_not_found(self):
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_players_from_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_not_found(self):
        players = self.stats.team("XXX")
        self.assertEqual(players, [])

    def test_top_orders_by_points(self):
        players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(
            [p.name for p in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_default_points(self):
        players = self.stats.top(3)
        self.assertEqual(
            [p.name for p in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_orders_by_goals(self):
        players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(
            [p.name for p in players],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_orders_by_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(
            [p.name for p in players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )

    def test_top_returns_requested_number(self):
        players = self.stats.top(2)
        self.assertEqual(len(players), 2)


if __name__ == "__main__":
    unittest.main()