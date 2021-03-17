from footyhints.config import config


def google_analytics(request):
    key = "None"
    if config.google_analytics_key:
        key = config.google_analytics_key
    return {
        'GOOGLE_ANALYTICS_KEY': key,
    }
