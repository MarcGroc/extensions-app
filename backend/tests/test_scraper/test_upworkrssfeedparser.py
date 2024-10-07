from django.test import TestCase

from scraper.models import JobPosting
from scraper.rss_feed_parser import UpworkRSSFeedParser

RSS_ENTRIES_COUNT = 30


class TestUpworkRSSFeedParser(TestCase):
    def setUp(self):
        self.parser = UpworkRSSFeedParser()

    def test_get_entries(self):
        entries = self.parser.get_entries()
        self.assertGreater(len(entries), 0)

    def test_parse_entries(self):
        entries = self.parser.parse_entries()
        self.assertGreater(len(entries), 0)
        self.assertIsInstance(entries[0], dict)

    def test_save_parsed_feed_to_db(self):
        self.parser.save_parsed_feed_to_db()
        self.assertEqual(JobPosting.objects.count(), RSS_ENTRIES_COUNT)

