from django.core.management import BaseCommand

from scraper.rss_feed_parser import UpworkRSSFeedParser


class Command(BaseCommand):
    help = 'Parses RSS feed and saves job postings to the database'

    def handle(self, *args, **kwargs):
        parser = UpworkRSSFeedParser()
        parser.process_feed()
