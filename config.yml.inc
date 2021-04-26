# Development
mode: development
db_uri: sqlite:////tmp/footyhints.db
web_debug: True

# # Production
# mode: production
# api_key: <insert_api_key>
# google_analytics_key: <insert_google_analytics_key>
# google_api_key: <insert_google_api_key>
# db_uri: mysql://user:pass@127.0.0.1/footyhints
# web_debug: False

cache_enabled: False
# cache_uri: redis://127.0.0.1:6379/1
# cache_expiration: 900

secret_key: 1234567890

# League to fetch for
fetch_league_country: England
fetch_league_name: Premier League
