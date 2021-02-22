from footyhints.plugin import Plugin


HIGH_PROFILE_TEAMS = [
    "Arsenal",
    "Chelsea",
    "Liverpool",
    "Manchester United",
    "Manchester City",
    "Tottenham",
]


class HighProfileMatchup(Plugin):
    priority = 1

    def score(self, game):
        if game.home_team.name in HIGH_PROFILE_TEAMS and game.away_team.name in HIGH_PROFILE_TEAMS:
            return 100, "Big matchup"
        else:
            return 0, "Not a big matchup"
