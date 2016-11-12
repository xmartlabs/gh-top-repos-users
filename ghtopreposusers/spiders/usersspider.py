# -*- coding: utf-8 -*-
import csv
import glob
import json
import scrapy


class UsersSpider(scrapy.Spider):
    name = 'users'

    start_urls = []
    for filename in glob.glob('users/*.csv'):
        with open(filename) as file:
            start_urls.extend('https://api.github.com/users/{}'.format(user) for user, _ in csv.reader(file))

    def parse(self, response):
        user = json.loads(response.text)
        yield {k: v for k, v in user.items() if not k.endswith('url')}
