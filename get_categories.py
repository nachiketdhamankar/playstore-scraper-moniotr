"""Stores all the categories supported by the play-store-scraper library

Houses all the categories supported by the play-store-scraper (https://pypi.org/project/play-scraper/) as a dictionary.
Created a seperate file for better readability.
"""

CATEGORIES = {
    "ART_AND_DESIGN": "ART_AND_DESIGN",
    "AUTO_AND_VEHICLES": "AUTO_AND_VEHICLES",
    "BEAUTY": "BEAUTY",
    "BOOKS_AND_REFERENCE": "BOOKS_AND_REFERENCE",
    "BUSINESS": "BUSINESS",
    "COMICS": "COMICS",
    "COMMUNICATION": "COMMUNICATION",
    "DATING": "DATING",
    "EDUCATION": "EDUCATION",
    "ENTERTAINMENT": "ENTERTAINMENT",
    "EVENTS": "EVENTS",
    "FINANCE": "FINANCE",
    "FOOD_AND_DRINK": "FOOD_AND_DRINK",
    "HEALTH_AND_FITNESS": "HEALTH_AND_FITNESS",
    "HOUSE_AND_HOME": "HOUSE_AND_HOME",
    "LIBRARIES_AND_DEMO": "LIBRARIES_AND_DEMO",
    "LIFESTYLE": "LIFESTYLE",
    "MAPS_AND_NAVIGATION": "MAPS_AND_NAVIGATION",
    "MEDICAL": "MEDICAL",
    "MUSIC_AND_AUDIO": "MUSIC_AND_AUDIO",
    "NEWS_AND_MAGAZINES": "NEWS_AND_MAGAZINES",
    "PARENTING": "PARENTING",
    "PERSONALIZATION": "PERSONALIZATION",
    "PHOTOGRAPHY": "PHOTOGRAPHY",
    "PRODUCTIVITY": "PRODUCTIVITY",
    "SHOPPING": "SHOPPING",
    "SOCIAL": "SOCIAL",
    "SPORTS": "SPORTS",
    "TOOLS": "TOOLS",
    "TRAVEL_AND_LOCAL": "TRAVEL_AND_LOCAL",
    "VIDEO_PLAYERS": "VIDEO_PLAYERS",
    "WEATHER": "WEATHER",
}


"""Returns a list of all categories supported by play-store-scraper library

Returns a list of all the values of all the categories supported by the library (dictionary above)
"""

def get_categories():
    return list(CATEGORIES.values())