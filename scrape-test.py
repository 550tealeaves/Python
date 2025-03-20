#Step 1 - Import libraries - must first install on local machine
        # In terminal, first type python --version
        # Then install requests libraries - python -m pip install requests
        ## This lets you make requests to site servers to grab data
        # Install beautifulsoup4 - python -m pip install beautifulsoup4


import requests #python -m pip install requests to install it (terminal)
from bs4 import BeautifulSoup # python -m pip install beautifulsoup4 (terminal)
import csv # already included in Python, don't have to install this externally 


# Create function to extract data
def get_country_data():
    url = "https://www.scrapethissite.com/pages/simple/" #this is website to scrape data
    response = requests.get(url)

    # Create code that handles if the scrape fails - prints error msg & returns empty list
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return []

    # Converts the raw HTML into a structured object (soup) that can be searched and analyzed using CSS selectors
    soup = BeautifulSoup(response.text, "html.parser")
    countries = []

    # Use for-loop to target the specific classes and elements that contain desired info
    for countries_data in soup.select(".country-name"):
        name_tag = countries_data.select_one("h3 i")
        if name_tag:
            name = name_tag.get_text(strip=True)
        else:
            continue

        #Pull the countries' capitals
        capital_tag = countries_data.select_one(".country-info")
        if capital_tag:
            capital = capital_tag.get_text(strip=True)
        else:
            capital = "No information on capital"

        #Pull the countries' populations
        pop_tag = countries_data.select_one(".country-population")
        if pop_tag:
            population = pop_tag.get_text(strip=True)
        else:
            population = "No information on population"

        #Pull the countries' areas
        area_tag = countries_data.select_one(".country-area")
        if area_tag:
            area = area_tag.get_text(strip=True)
        else:
            area = "No information on area"


        #Create dictionary that contains all extracted information
        countries.append({"name": name, "capital": capital, "population": population, "area": area})

    return countries #must be run outside of for loop


# Create new function to save list as CSV file
def save_to_csv(countries, filename="countries-info"): #name csv file
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "capital", "population", "area"])
        writer.writeheader()
        writer.writerows(countries)


#Execute single script
if __name__ == "__main__":
    country_information = get_country_data()
    for country in country_information:
        print(country)
    save_to_csv(country_information)
