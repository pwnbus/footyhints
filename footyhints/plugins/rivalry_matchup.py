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


class RivalryMatchup(Plugin):
    description = 'Rivalry Matchup'

    def score(self):
        for matchup in MATCHUPS:
            if self.game.home_team.name in matchup[0] and self.game.away_team.name in matchup[1]:
                return 100, "Rivalry matchup"
            elif self.game.away_team.name in matchup[0] and self.game.home_team.name in matchup[1]:
                return 100, "Rivalry matchup"
        return 0, "Not a rivalry matchup"
