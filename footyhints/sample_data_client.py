from random import randint, shuffle


class SampleDataClient():
    def get_results(self):
        teams = [
            'AFC Bournemouth',
            'Arsenal FC',
            'Aston Villa FC',
            'Brighton & Hove Albion FC',
            'Burnley FC',
            'Chelsea FC',
            'Crystal Palace FC',
            'Everton FC',
            'Leicester City FC',
            'Liverpool FC',
            'Manchester City FC',
            'Manchester United FC',
            'Newcastle United FC',
            'Norwich City FC',
            'Sheffield United FC',
            'Southampton FC',
            'Tottenham Hotspur FC',
            'Watford FC',
            'West Ham United FC',
            'Wolverhampton Wanderers FC'
        ]
        results = []
        num_match_days = randint(5, 38)
        for match_day in range(1, num_match_days + 1):
            temp_team_names = [team[:] for team in teams]
            shuffle(temp_team_names)
            while len(temp_team_names) != 0:
                home_team = temp_team_names.pop()
                away_team = temp_team_names.pop()
                results.append({
                    "home_team": home_team,
                    "away_team": away_team,
                    "home_score": randint(0, randint(0, 7)),
                    "away_score": randint(0, randint(0, 7)),
                    "match_day": match_day
                })

        return results
