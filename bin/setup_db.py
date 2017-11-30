from footyhints.config import config

from import_pl_data import import_production_data
from import_sample_data import import_development_data

if config.mode == 'production':
    import_production_data()
else:
    import_development_data()
