#Step 1 - Import libraries - must first install on local machine
        # In terminal, first type python --version
        # Then install requests libraries - python -m pip install requests
        ## This lets you make requests to site servers to grab data
        # Install beautifulsoup4 - python -m pip install beautifulsoup4


import requests #python -m pip install requests to install it (terminal)
from bs4 import BeautifulSoup # python -m pip install beautifulsoup4 (terminal)
import csv # already included in Python, don't have to install this externally 



def get_ny_assembly_members():
    url = "https://nyassembly.gov/mem/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return [] # If the request fails (i.e., status code is not 200), it prints an error message and returns an empty list ([]), stopping further execution
    
    soup = BeautifulSoup(response.text, "html.parser") # Converts the raw HTML into a structured object (soup) that can be searched and analyzed using CSS selectors.
    members = []
    
    for member_card in soup.select(".mem-item"): # Selects all the elements with the class name "mem-item" (i.e., the cards containing information about each member) and iterates over them        
        name_tag = member_card.select_one("h3 a") # Selects the first <a> tag inside the <h3> tag in the current member card, NO COMMAS b/w elements
        if name_tag: 
            name = name_tag.get_text(strip=True) # Extracts the text from the tag and removes any leading/trailing whitespaces
            profile_url = "https://nyassembly.gov" + name_tag["href"] # Extracts the value of the "href" attribute from the tag and appends it to the base URL
        else:
            continue # If the name tag is not found, it skips the current iteration and moves to the next member card
        
        contact_info = member_card.select_one(".mem-email") 
        if contact_info:
            contact = contact_info.get_text(strip=True) # Extracts the text from the tag and removes any leading/trailing whitespaces
        else:
            contact = "No contact info available"
    
        members.append({"name": name, "profile_url": profile_url, "contact": contact}) # Appends a dictionary containing the name, profile URL, and contact information of the current member to the list of members
    
    return members # Returns the list of members

def save_to_csv(members, filename="ny_assembly_members.csv"): # Saves the list of members to a CSV file
    with open(filename, mode="w", newline="", encoding="utf-8") as file: 
        writer = csv.DictWriter(file, fieldnames=["name", "profile_url", "contact"]) # Creates a CSV writer object with the specified fieldnames
        writer.writeheader() # Writes the header row to the CSV file
        writer.writerows(members) # Writes the data rows to the CSV file

if __name__ == "__main__":
    assembly_members = get_ny_assembly_members()
    for member in assembly_members:
        print(member)
    save_to_csv(assembly_members)
    print(f"Saved {len(assembly_members)} members to ny_assembly_members.csv")

# Challenge: Extract Full Address
# Modify the code to also extract the full address of each assembly member and include it in the CSV file.
# Hint: Look for an element on the webpage that contains address information, extract it, and update the `members` dictionary.