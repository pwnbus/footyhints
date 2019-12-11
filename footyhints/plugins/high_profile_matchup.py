from footyhints.plugin import Plugin


HIGH_PROFILE_TEAMS = [
    "Arsenal FC",
    "Chelsea FC",
    "Liverpool FC",
    "Manchester United FC",
    "Manchester City FC",
    "Tottenham Hotspur FC",
]


class HighProfileMatchup(Plugin):
    description = 'High Profile Matchups'

    def score(self):
        if self.game.home_team.name in HIGH_PROFILE_TEAMS and self.game.away_team.name in HIGH_PROFILE_TEAMS:
            return 100, "Big matchup"
        else:
            return 0, "Not a big matchup"
