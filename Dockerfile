FROM python:3.5.2-onbuild
CMD ["scrapy", "crawl", "topreposusers", "-o", "output/output.json"]
