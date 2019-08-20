#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to scrape Google Play Store and save information about apps per category for different countries.

Scrapes (using Play Store Scraper - see requirements.txt) the information about the top 100 apps for each category in India and United States of America.
Stores the detailed information about each app in the /output/app_info/ folder (each category and country has it's own JSON file)
It also calculates the number of installs (in thousands) per category in a country ( as a Summary ) and stores in /output/installs_per_category_for_100.json - when top 100 apps are considered.

Install all the requirements from requirements.txt before running this script.
To change any arguments or parameters, refer the play-scraper documentation at - https://pypi.org/project/play-scraper/
"""

import play_scraper
from get_categories import get_categories
import re
import json
from tqdm import tqdm


# The countries to be considered. List of available countries is found here - https://github.com/danieliu/play-scraper/blob/master/play_scraper/constants.py#L87 
countries = ['in', 'us']

# The number of downloads considered. Top 100 apps are considered in this case.
number_of_results = 100

# Fetches the categories from 'get_categories()'
categories = get_categories()
downloads_per_country_per_category = {}

for category in tqdm(categories):
    downloads_per_country_by_category = {}

    # Print the category that is being scraped
    tqdm.write('Category: %s ' % category)

    for country in countries:
        # For each category and each country, scrape the play store and write the information to output/app_info/ foler (according to the appropriate file name)
        list_top_n_apps_by_categry = \
            play_scraper.collection(collection='TOP_FREE', gl=country,
                                    category=category,
                                    results=number_of_results,
                                    detailed=True)

        # Write to output/app_info/{country}_{category}_{number_of_results}.json
        with open('output/app_info/%s_%s_%s.json' % (country, category,
                  number_of_results), 'w', encoding='utf-8') as \
            file_pointer:
            json.dump(list_top_n_apps_by_categry, file_pointer,
                      indent=4)

        # Find the number of installs (in thousands) for each app in each country and category.
        installs = [int(re.sub('[,+]', '', app['installs']))/1000 for app in
                    list_top_n_apps_by_categry]
                    
        # Find the sum of number of downloads for each country for each category.
        downloads_per_country_by_category[country] = sum(installs)
        
        # Print the country for the category that's being scraped
        tqdm.write('\tCountry: %s -> Done' % country)
    
    # Store the number of downloads ( in 1000s ) for each country and category in a dictionary.
    downloads_per_country_per_category[category] = \
        downloads_per_country_by_category

# Save the dictionary created above in output/installs_per_category_for_100.json - when top 100 apps are considred.
with open('output/installs_per_category_for_%s.json' % (number_of_results), 'w', encoding='utf-8') as file_pointer:
    json.dump(downloads_per_country_per_category, file_pointer, indent=4)