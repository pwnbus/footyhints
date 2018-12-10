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
        assert type(self.mock_obj.call_args[1]['league_country']) is str
        assert self.mock_obj.call_args[1]['league_country'] is not ""
        assert type(self.mock_obj.call_args[1]['league_name']) is str
        assert self.mock_obj.call_args[1]['league_name'] is not ""
        assert resp.status_code == 200

    def test_index_slash(self):
        resp = self.client.get('/')
        self.verify_index(resp)

    def test_index(self):
        resp = self.client.get('/index')
        self.verify_index(resp)
