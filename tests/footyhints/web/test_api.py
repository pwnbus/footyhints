from json import loads

from tests.footyhints.web.web_test import WebTest


class TestApi(WebTest):

    def setup(self):
        super().setup()
        self.game.set_score(3, 3)
        self.session.add(self.game)
        self.session.commit()

    def test_api_games(self):
        self.game.worth_watching()
        self.session.add(self.game)
        self.session.commit()
        games_resp = self.client.get('/api/games')
        table_obj = loads(games_resp.data.decode('utf8'))
        assert len(table_obj) == 1
        row_obj = table_obj['data'][0]
        assert type(row_obj['interest_score']) is int
        assert type(row_obj['interest_level']) is str
        assert row_obj['round_num'] == 1
        assert row_obj['game_id'] == 1
        assert row_obj['home_team'] == 'Chelsea'
        assert row_obj['away_team'] == 'Manchester United'
        assert len(row_obj['score_modifications']) > 0
        for score_modification in row_obj['score_modifications']:
            assert score_modification[0] >= 0
            assert type(score_modification[1]) is str
