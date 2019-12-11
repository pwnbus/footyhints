from footyhints.plugin import Plugin


MATCHUPS = [
    ["Arsenal FC", "Tottenham Hotspur FC"],
    ["Arsenal FC", "Chelsea FC"],
    ["Chelsea FC", "Tottenham Hotspur FC"],
    ["Chelsea FC", "West Ham United FC"],
    ["Liverpool FC", "Everton FC"],
    ["Liverpool FC", "Manchester United FC"],
    ["Manchester City FC", "Manchester United FC"],
]


class HighProfileMatchup(Plugin):
    description = 'High Profile Matchups'
    # Max score would be a match on matchups
    max_score = 100
    # Min Score would be a non matchup

    def score(self):
        for matchup in MATCHUPS:
            if self.game.home_team.name in matchup[0] and self.game.away_team.name in matchup[1]:
                return self.max_score
            elif self.game.away_team.name in matchup[0] and self.game.home_team.name in matchup[1]:
                return self.max_score
        return 0
