# -*- coding: utf-8 -*-
import json
import math
import scrapy

MAX_ITEMS_TO_FETCH = 5000
RESULTS_PER_PAGE = 100


class TopReposUsersSpider(scrapy.Spider):
    name = 'topreposusers'
    start_urls = ['https://api.github.com/search/repositories?q=stars:>1&page={}'.format(page)
                  for page in range(1, math.ceil(MAX_ITEMS_TO_FETCH / RESULTS_PER_PAGE) + 1)]

    def parse(self, response):
        for repository in json.loads(response.text)['items']:
            yield scrapy.Request('https://api.github.com/repos/{}/contributors'.format(repository['full_name']),
                                 callback=TopReposUsersSpider.parse_contributors)

    @staticmethod
    def parse_contributors(response):
        for contributor in json.loads(response.text):
            yield scrapy.Request(contributor['url'], callback=TopReposUsersSpider.parse_user)

    @staticmethod
    def parse_user(response):
        yield json.loads(response.text)
