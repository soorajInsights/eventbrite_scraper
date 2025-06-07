# Eventbrite Scraper

A Scrapy-based web scraper to extract event details from Eventbrite (Ernakulam, India) and save the output as JSON.

---

## Prerequisites

Install Scrapy using pip:

```bash
pip install scrapy
```

---

## Project Structure

```
eventbrite_scraper/
├── scrapy.cfg
├── eventbrite_scraper/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       └── eventbrite.py
├── events.json   # output file generated after running the spider
```

---

## How to Run

From your terminal, navigate to the project root directory (where `scrapy.cfg` is located), then run:

```bash
scrapy crawl eventbrite
```

---

## Output

The scraped data will be saved to:

```
events.json
```

in the project root directory.
