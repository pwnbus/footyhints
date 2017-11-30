from random import randint, shuffle

from footyhints.models.team import Team
from footyhints.models.round import Round
from footyhints.models.game import Game

from footyhints.db import session, create_db, delete_db


def import_development_data():
    team_names = [
        'Chelsea',
        'Tottenham Hotspur',
        'Manchester City',
        'Liverpool',
        'Arsenal',
        'Manchester United',
        'Everton',
        'Southampton',
        'Bournemouth',
        'West Bromwich Albion',
        'West Ham United',
        'Leicester City',
        'Stoke City',
        'Crystal Palace',
        'Swansea City',
        'Burnley',
        'Watford',
        'Hull City',
        'Middlesbrough',
        'Sunderland',
    ]

    teams = {}
    for team_name in team_names:
        team = Team(name=team_name)
        teams[team_name] = team

    num_rounds = randint(1, 38)
    for num in range(1, num_rounds + 1):
        temp_team_names = [team[:] for team in team_names]
        shuffle(temp_team_names)
        round = Round(num)
        print("Match Day: {}".format(round.num))
        while len(temp_team_names) != 0:
            home_team = teams[temp_team_names.pop()]
            away_team = teams[temp_team_names.pop()]
            game = Game(home_team=home_team, away_team=away_team, round=round)
            game.set_score(randint(0, randint(0, 7)), randint(0, randint(0, 7)))
            game.worth_watching()
            print("\tCreating game\t{0} | {1}\t{2}-{3}".format(home_team.name, away_team.name, game.home_team_score, game.away_team_score))
            session.add(game)
            session.add(home_team)
            session.add(away_team)
        session.add(round)
    session.commit()
    session.close()


if __name__ == '__main__':
    print("Setting up DB")
    delete_db()
    create_db()
    import_development_data()