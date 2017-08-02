from tests.footyhints.web.web_test import WebTest


class TestIndex(WebTest):

    def setup(self):
        super().setup()
        self.game.set_score(3, 3)
        self.session.add(self.game)
        self.session.commit()

    def verify_index(self, resp):
        assert len(self.mock_obj.call_args) == 2
        assert self.mock_obj.call_args[0][0] == 'index.html'
        assert self.mock_obj.call_args[1]['season_name'] == 'Premier League 2016/17'
        assert resp.status_code == 200

    def test_index_slash(self):
        resp = self.client.get('/')
        self.verify_index(resp)

    def test_index(self):
        resp = self.client.get('/index')
        self.verify_index(resp)
