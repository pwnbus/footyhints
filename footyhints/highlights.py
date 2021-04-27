import datetime

from youtubesearchpython import VideosSearch
from footyhints.logger import logger
from footyhints.config import config


def get_highlights_url(game):
    if config.mode.lower() == 'production':
        game_date = datetime.datetime.fromtimestamp(game['start_time']).strftime('%d/%m/%Y')
        game_search_str = "{} v. {} | PREMIER LEAGUE HIGHLIGHTS | {} | NBC Sports".format(
            game['home_team'],
            game['away_team'],
            game_date,
        )
        logger.debug("Searching youtube for highlights video {} \t{} vs {}".format(game_date, game['home_team'], game['away_team']))
        search = VideosSearch(game_search_str, limit=1)
        return 'https://www.youtube.com/embed/{}'.format(search.result()['result'][0]['id'])
    return 'https://www.youtube.com/embed/o1LAo78O8w8'
