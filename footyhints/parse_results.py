from footyhints.models.team import Team
from footyhints.models.game import Game
from footyhints.models.competition import Competition

from footyhints.db import session
from footyhints.decision_maker import DecisionMaker
from footyhints.config import config


class ParseResults():
    def __init__(self, update=False):
        self.update = update

    def create_teams(self, results):
        teams = {}
        if self.update:
            db_teams = session.query(Team).all()
            for team in db_teams:
                teams[team.name] = team
            return teams
        home_teams = [result['home_team'] for result in results]
        away_teams = [result['away_team'] for result in results]
        team_names = set(home_teams + away_teams)
        for team_name in team_names:
            team = Team(name=team_name)
            teams[team_name] = team
            session.add(team)
        session.commit()
        return teams

    def get_competition(self):
        competition = Competition(name=config.fetch_league_name)
        if self.update:
            competition_db = session.query(Competition).one()
            if competition_db:
                competition = competition_db
        return competition

    def parse_results(self, results):
        teams = self.create_teams(results)
        decision_maker = DecisionMaker()
        competition = self.get_competition()

        for match in results:
            if self.update:
                home_team = session.query(Team).filter(Team.name == match['home_team']).one()
                game_found = session.query(Game).filter(Game.match_day == match['match_day']).filter(Game.home_team == home_team).all()
                if game_found:
                    continue
            game = Game(
                home_team=teams[match['home_team']],
                away_team=teams[match['away_team']],
                match_day=match['match_day'],
                start_time=match['start_time'],
                competition=competition,
            )
            game.set_score(match['home_score'], match['away_score'])
            print("Creating game\t{0} | {1}\t{2}-{3} ({4})".format(
                match['home_team'],
                match['away_team'],
                game.home_team_score,
                game.away_team_score,
                game.match_day
            ))
            decision_maker.worth_watching(game)
            session.add(game)
        competition.update_timestamp()
        session.add(competition)
        session.commit()
        session.close()
