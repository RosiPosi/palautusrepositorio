from rich.console import Console
from rich.table import Table
from player import PlayerReader, PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    team = input("Give team abbreviation: ").strip().upper()
    players = stats.top_scorers_by_team(team)

    console = Console()
    table = Table(title=f"{team} players 2024-2025")

    table.add_column("Name", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", style="green")
    table.add_column("Assists", style="green")
    table.add_column("Points", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assist),
            str(player.total)
        )

    console.print(table)

if __name__ == "__main__":
    main()
