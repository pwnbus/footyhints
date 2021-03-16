from footyhints.score_plugin import ScorePlugin


class HighProfileMatchup(ScorePlugin):
    priority = 1
    required_num_games = 3

    def score(self, game):
        if game.home_team.played < self.required_num_games or game.away_team.played < self.required_num_games:
            return 0, "Too Early in Season"

        if game.home_team.place <= 6 and game.away_team.place <= 6:
            return 100, "Top 6 matchup ({} v {})".format(game.home_team.place, game.away_team.place)

        if game.home_team.place >= 15 and game.away_team.place >= 15:
            return 100, "Fight for relegation battle ({} v {})".format(game.home_team.place, game.away_team.place)

        place_delta = abs(game.home_team.place - game.away_team.place)
        if place_delta <= 3:
            return 100, "Within 3 places in the table ({} v {})".format(game.home_team.place, game.away_team.place)
        elif place_delta <= 6:
            return 50, "Within 6 places in the table ({} v {})".format(game.home_team.place, game.away_team.place)
        elif place_delta <= 9:
            return 10, "Within 9 places in the table ({} v {})".format(game.home_team.place, game.away_team.place)
        else:
            return -50, "Not a big game ({} v {})".format(game.home_team.place, game.away_team.place)
