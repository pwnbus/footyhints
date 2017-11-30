from footyhints.config import config

from import_pl_data import import_production_data
from import_sample_data import import_development_data
from footyhints.db import create_db, delete_db

print("Setting up DB")
delete_db()
create_db()

if config.mode == 'production':
    import_production_data()
else:
    import_development_data()
