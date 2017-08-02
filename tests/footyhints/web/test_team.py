from tests.footyhints.web.web_test import WebTest


class TestTeam(WebTest):

    def setup(self):
        super().setup()
        self.game.set_score(3, 3)
        self.session.add(self.game)
        self.session.commit()

    def verify_team(self, resp, team_name):
        assert len(self.mock_obj.call_args) == 2
        assert self.mock_obj.call_args[0][0] == 'team.html'
        assert self.mock_obj.call_args[1]['team'].name == team_name
        assert resp.status_code == 200

    def test_chelsea_team(self):
        resp = self.client.get('/team/1')
        self.verify_team(resp, 'Chelsea')

    def test_united_team(self):
        resp = self.client.get('/team/2')
        self.verify_team(resp, 'Manchester United')
