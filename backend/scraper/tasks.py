from celery import shared_task
from scraper.models import JobPosting
from loguru import logger
from scraper.rss_feed_parser import UpworkRSSFeedParser
@shared_task
def get_job_postings():
    logger.info("Getting job postings")
    rss_feed_parser = UpworkRSSFeedParser()
    rss_feed_parser.process_feed()