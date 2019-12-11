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
    # Max score would be a match on matchups
    max_score = 100
    # Min Score would be a non matchup

    def score(self):
        if self.game.home_team.name in HIGH_PROFILE_TEAMS and self.game.away_team.name in HIGH_PROFILE_TEAMS:
            return self.max_score
        else:
            return 0
