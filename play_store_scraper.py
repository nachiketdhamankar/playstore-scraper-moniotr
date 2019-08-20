#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Intro to what code does  - broad
"""
import play_scraper
from get_categories import get_categories
import re
import json

countries = ['in', 'us']
number_of_results = 100
categories = get_categories()
downloads_per_country_per_category = {}

for category in categories:
    downloads_per_country_by_category = {}
    for country in countries:
        list_top_n_apps_by_categry = \
            play_scraper.collection(collection='TOP_FREE', gl=country,
                                    category=category,
                                    results=number_of_results,
                                    detailed=True)

        # Write to output/app_info/{country}_{category}_{number_of_results}.json
        with open('output/app_info2/%s_%s_%s.json' % (country, category,
                  number_of_results), 'w', encoding='utf-8') as \
            file_pointer:
            json.dump(list_top_n_apps_by_categry, file_pointer,
                      indent=4)

        installs = [int(re.sub('[,+]', '', app['installs']))/1000 for app in
                    list_top_n_apps_by_categry]
        downloads_per_country_by_category[country] = sum(installs)
    downloads_per_country_per_category[category] = \
        downloads_per_country_by_category

with open('output/installs_per_category_for_%s.json' % (number_of_results), 'w', encoding='utf-8') as file_pointer:
    json.dump(downloads_per_country_per_category, file_pointer, indent=4)