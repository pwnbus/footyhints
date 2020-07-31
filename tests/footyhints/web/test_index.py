from tests.footyhints.web.web_test import WebTest


class TestIndex(WebTest):

    def verify_index(self, resp):
        assert len(self.mock_obj.call_args) == 2
        assert self.mock_obj.call_args[0][0] == 'index.html'
        assert type(self.mock_obj.call_args[1]['games']) == list
        assert len(self.mock_obj.call_args[1]['games']) == 1
        assert resp.status_code == 200

    def test_index_slash(self):
        resp = self.client.get('/')
        self.verify_index(resp)

    def test_index(self):
        resp = self.client.get('/index')
        self.verify_index(resp)
