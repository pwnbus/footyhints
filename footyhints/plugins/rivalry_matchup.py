from footyhints.plugin import Plugin


MATCHUPS = [
    ["Arsenal", "Tottenham"],
    ["Arsenal", "Chelsea"],
    ["Chelsea", "Tottenham"],
    ["Chelsea", "West Ham"],
    ["Liverpool", "Everton"],
    ["Liverpool", "Manchester United"],
    ["Manchester City", "Manchester United"],
]


class RivalryMatchup(Plugin):
    priority = 1

    def score(self, game):
        for matchup in MATCHUPS:
            if game.home_team.name in matchup[0] and game.away_team.name in matchup[1]:
                return 100, "Rivalry matchup"
            elif game.away_team.name in matchup[0] and game.home_team.name in matchup[1]:
                return 100, "Rivalry matchup"
        return 0, "Not a rivalry matchup"
