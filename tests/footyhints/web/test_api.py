from json import loads

from tests.footyhints.web.web_test import WebTest


class TestApi(WebTest):

    def setup(self):
        super().setup()
        self.game.set_score(3, 3)
        self.session.add(self.game)
        self.session.commit()

    def verify_games_resp(self, games_resp):
        table_obj = loads(games_resp.data.decode('utf8'))
        assert len(table_obj) == 1
        row_obj = table_obj['data'][0]
        assert type(row_obj['interest_score']) is int
        assert type(row_obj['interest_level']) is str
        assert row_obj['round_num'] == 1
        assert row_obj['game_id'] == 1
        assert row_obj['home_team_name'] == 'Chelsea'
        assert row_obj['home_team_id'] == 1
        assert row_obj['away_team_name'] == 'Manchester United'
        assert row_obj['away_team_id'] == 2
        assert len(row_obj['score_modifications']) > 0
        for score_modification in row_obj['score_modifications']:
            assert score_modification[0] >= 0
            assert type(score_modification[1]) is str

    def test_api_games_all(self):
        self.game.worth_watching()
        self.session.add(self.game)
        self.session.commit()
        games_resp = self.client.get('/api/games/all')
        self.verify_games_resp(games_resp)

    def test_api_team_games(self):
        self.game.worth_watching()
        self.session.add(self.game)
        self.session.commit()
        games_resp = self.client.get('/api/team/1/games')
        self.verify_games_resp(games_resp)
