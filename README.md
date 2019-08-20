# Play Store Scraper & Analyzer

This project scrapes the Google Play Store and saves information about apps per category for the specified countries. The data is stored in JSON format.
Scrapes (using [Play Store Scraper](https://pypi.org/project/play-scraper/) - see requirements.txt) the information about the top 100 apps for each category in India and United States of America.
Stores the detailed information about each app in the /output/app_info/ folder (each category and country has it's own JSON file)
It also calculates the number of installs (in thousands) per category in a country ( as a Summary ) and stores in */output/installs_per_category_for_100.json* - when top 100 apps are considered.

### Installation

Make sure you have the following installed 
- Python (3+) : [Download link](https://www.python.org/downloads/release/python-370/)
- Pipenv : [Download link](https://docs.pipenv.org/en/latest/)

To clone this repository using -

<!-- $ git clone --single-branch --branch migrate_to_pip https://github.com/nachiketdhamankar/playstore-scraper-moniotr.git -->
```powershell
$ git clone https://github.com/nachiketdhamankar/playstore-scraper-moniotr.git
$ cd playstore-scraper-moniotr
```

To install the required library and activate the virtual environment - 
```powershell
pipenv install -r requirements.txt
pipenv shell
```

To run the Play Store Scraper - 
```powershell
python play_store_scraper.py
```

Once you run the script, run the notebook to plot the data using -
```powershell
jupyter notebook 'Plotting Data.ipynb'
```

Make sure to run all the cells in the notebook - [how to run all cells in a notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html#executing-a-notebook)