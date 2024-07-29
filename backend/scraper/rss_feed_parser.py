import re
from datetime import datetime
from typing import Optional, Any

import feedparser
from django.core.exceptions import ValidationError
from django.utils.timezone import make_aware
from loguru import logger

from scraper.models import JobPosting

RSS_FILE = r"rss.txt"  # test file
UPWORK_RSS_FEED = ("https://www.upwork.com/ab/feed/jobs/rss?paging=NaN-undefined&q=(chrome%20AND%20extension)%20OR("
                   "browser%20AND%20extension)&sort=recency&api_params=1&securityToken"
                   "=ff0603605bb09c5702dbf7322f6c7574bad1b6d1c659dceecaf69ee59989293141057411870bd7c2eaf108b27d3582c5dfa14acb5542b0aa03eaf273a7d72894&userUid=1560698319152050176&orgUid=1560698319152050177")


class UpworkRSSFeedParser:
    def __init__(self):
        self.feed_url = UPWORK_RSS_FEED
        self.feed_file = RSS_FILE
        self.entries = self.get_entries()
        self.parsed_data = self.parse_entries()

    def get_entries(self):
        if self.feed_url:
            return self.get_entries_from_url()
        elif self.feed_file:
            return self.get_entries_from_file()
        else:
            logger.exception('No feed_url or feed_file provided')

    def get_entries_from_file(self):
        logger.warning(f'Getting RSS Feed from file {self.feed_file}')
        try:
            with open(self.feed_file, 'r') as f:
                rss_data = feedparser.parse(f.read())
            return rss_data.entries
        except FileNotFoundError:
            logger.exception(f'File {self.feed_file} not found')

    def get_entries_from_url(self):
        logger.warning(f'Getting RSS Feed from URL {self.feed_url[:30]}')
        try:
            rss_data = feedparser.parse(self.feed_url)
            return rss_data.entries
        except ConnectionError:
            logger.exception(f'Failed to get RSS Feed from URL {self.feed_url}')
        except Exception as e:
            logger.exception(f'Failed to get RSS Feed from URL {self.feed_url}: {e}')

    def parse_entries(self):
        logger.info('Parsing RSS Feed')
        parsed_entries = []
        for entry in self.entries:
            parsed_entry = self.parse_single_entry(entry)
            if parsed_entry:
                parsed_entries.append(parsed_entry)
        return parsed_entries

    def parse_single_entry(self, entry: feedparser.FeedParserDict) -> Optional[dict[str, Any]]:
        try:
            skills_match = re.search(r'Skills</b>:(.*?)(<br />|</p>)', entry.description, re.DOTALL)
            budget_match = re.search(r'Budget</b>:\s*\$(\d+)', entry.description)
            category_match = re.search(r'Category</b>:(.*?)(<br />|</p>)', entry.description)
            country_match = re.search(r'Country</b>:(.*?)(<br />|</p>)', entry.description)
            posted_on_match = re.search(r'Posted On</b>:(.*?)(<br />|</p>)', entry.description)

            skills = [skill.strip() for skill in skills_match.group(1).split(',')] if skills_match else []
            budget = float(budget_match.group(1)) if budget_match else None
            category = category_match.group(1).strip() if category_match else ''
            country = country_match.group(1).strip() if country_match else ''
            posted_on = self.parse_datetime(posted_on_match.group(1).strip()) if posted_on_match else None

            return {
                'guid': entry.get('id', ''),
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'description': entry.get('description', ''),
                'skills': skills,
                'budget': budget,
                'category': category,
                'country': country,
                'posted_on': posted_on,
            }
        except Exception as e:
            logger.exception(f"Error parsing entry: {str(e)}")
            return None

    def parse_datetime(self, date: str):
        try:
            dt = datetime.strptime(date, "%B %d, %Y %H:%M UTC")
            return make_aware(dt)
        except ValueError:
            logger.exception(f"Invalid date format: {date}")
            return None

    def save_parsed_feed_to_db(self):
        logger.info('Saving parsed RSS Feed to DB')
        for entry in self.parsed_data:
            try:
                job_posting, created = JobPosting.objects.update_or_create(
                    guid=entry['guid'],
                    defaults={
                        'title': entry['title'],
                        'link': entry['link'],
                        'description': entry['description'],
                        'category': entry['category'],
                        'budget': entry['budget'],
                        'posted_on': entry['posted_on'],
                        'country': entry['country'],
                        'skills': ', '.join(entry['skills']),
                    }
                )
                if created:
                    logger.info(f"Created new job posting: {entry['title']}")
            except ValidationError as e:
                logger.exception(f"Validation error when saving job posting: {str(e)}")
            except Exception as e:
                logger.exception(f"Error saving job posting: {str(e)}")

        logger.success('RSS Feed saved to DB successfully')

    def process_feed(self):
        self.get_entries()
        self.parse_entries()
        self.save_parsed_feed_to_db()
