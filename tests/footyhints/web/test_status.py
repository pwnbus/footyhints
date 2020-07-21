from tests.footyhints.web.web_test import WebTest


class TestStatus(WebTest):

    def verify_status(self, resp):
        assert len(self.mock_obj.call_args) == 2
        assert self.mock_obj.call_args[0][0] == 'status.html'
        assert resp.status_code == 200
        assert 'last_updated' in self.mock_obj.call_args[1]

    def test_status(self):
        resp = self.client.get('/status')
        self.verify_status(resp)
