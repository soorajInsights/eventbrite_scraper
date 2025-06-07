import scrapy
from urllib.parse import urljoin


class EventbriteSpider(scrapy.Spider):
    name = "eventbrite"
    allowed_domains = ["eventbrite.com"]
    start_urls = ["https://www.eventbrite.com/d/india--ernakulam/all-events/"]

    custom_settings = {
        'USER_AGENT': ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"),
        'ITEM_PIPELINES': {
            'eventbrite_scraper.pipelines.EventbritePipeline': 300,
        }
    }

    def parse(self, response):
        seen_urls = set()

        sections = response.css('section.event-card-details')

        for section in sections:
            try:
                event_div = section.css('div.Stack_root__1ksk7')
                if not event_div:
                    continue

                a_tag = event_div.css('a::attr(href)').get()
                if not a_tag:
                    continue

                source_url = urljoin(response.url, a_tag.strip())
                if source_url in seen_urls:
                    continue
                seen_urls.add(source_url)

                event_title = section.css('h3::text').get()
                event_title = event_title.strip() if event_title else "N/A"

                p_tags = event_div.css('p::text').getall()
                date_time = p_tags[0].strip() if len(p_tags) > 0 else "N/A"
                location = p_tags[1].strip() if len(p_tags) > 1 else "N/A"

                price_p = section.css('div.DiscoverHorizontalEventCard-module__priceWrapper___3rOUY p::text').get()
                ticket_price = price_p.strip() if price_p else "N/A"

                yield {
                    "source_url": source_url,
                    "event_title": event_title,
                    "date_time": date_time,
                    "location": location,
                    "ticket_price": ticket_price
                }

            except Exception as e:
                self.logger.error(f"Error parsing event: {e}")
