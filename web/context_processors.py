from footyhints.config import config


def google_analytics(request):
    if config.google_analytics_key:
        return {
            'GOOGLE_ANALYTICS_KEY': config.google_analytics_key,
        }
    return {}
