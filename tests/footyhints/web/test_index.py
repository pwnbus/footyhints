from tests.footyhints.web.web_test import WebTest


class TestIndex(WebTest):

    def setup(self):
        super(TestIndex, self).setup()
        self.game.set_score(3, 3)
        self.db.save(self.game)

    def test_index_slash(self):
        resp = self.client.get('/')
        assert self.mock_obj.call_args == self.build_args('index.html', games=[self.game])
        assert resp.status_code == 200

    def test_index(self):
        resp = self.client.get('/index')
        assert self.mock_obj.call_args == self.build_args('index.html', games=[self.game])
        assert resp.status_code == 200
