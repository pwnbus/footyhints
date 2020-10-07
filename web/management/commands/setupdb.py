from django.core.management.base import BaseCommand
from footyhints.sample_data_client import SampleDataClient
from footyhints.data_client import DataClient
from footyhints.parse_results import ParseResults
from footyhints.config import config


class Command(BaseCommand):
    help = 'Setup DB'

    def add_arguments(self, parser):
        parser.add_argument(
            '--update',
            action='store_true',
            dest='update',
            default=False,
            help='Update without removing the existing data',
        )

    def handle(self, *args, **options):
        client = SampleDataClient()
        if config.mode == 'production':
            client = DataClient()

        results = client.get_results()
        parser = ParseResults(config.fetch_league_country, config.fetch_league_name, options['update'])
        parser.parse_results(results)
