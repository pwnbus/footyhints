from tests.footyhints.web.web_test import WebTest


class TestIndex(WebTest):

    def setup(self):
        super().setup()
        self.game.set_score(3, 3)
        self.db.save(self.game)
        self.expected_game = {
            "home_team": "Chelsea",
            "away_team": "Manchester United",
            "interest_level": "High",
        }

    def test_index_slash(self):
        resp = self.client.get('/')
        assert self.mock_obj.call_args == self.build_args('index.html', games=[self.expected_game])
        assert resp.status_code == 200

    def test_index(self):
        resp = self.client.get('/index')
        assert self.mock_obj.call_args == self.build_args('index.html', games=[self.expected_game])
        assert resp.status_code == 200
