#STEP 1 - INSTALL LIBRARIES - must first install on local machine
        # In terminal, first type python --version
        # Then install requests libraries - python -m pip install requests
        ## This lets you make requests to site servers to grab data
        # Install beautifulsoup4 - python -m pip install beautifulsoup4
        # Don't have to do this multiple times

import requests
from bs4 import BeautifulSoup
import csv

# STEP 2 - CREATE FUNCTION THAT WILL SCRAPE DATA
    # Not giving it any arguments 
def get_ny_assembly_members():
    url = "https://nyassembly.gov/mem/" #Save url as variable
    response = requests.get(url) #Makes get request of everything on the website page

    # Write what happens if we don't get the response - do this so we aren't stuck in endless loop
    if response.status_code != 200: # if status code of response does not equal 200
        print("Webpage not retrieved") #print out this message
        return [] # return an empty list

    # STEP 3 - CREATE SOUP OBJECT
        ## Include the text and the html parser as a soup object - this is found in Beautiful soup docs - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    soup = BeautifulSoup(response.text, "html.parser") 
    members = [] #store the info on members in an empty list

    # STEP 4 - INSPECT WEBSITE
        #Look at web page to see where the desired information is located
        # we want name, email, and website of each member
        # Target section class="mem-item" that is the parent element that contains everything

    # STEP 5 - CREATE FOR-LOOP
        # Use for-loop to target class="mem-item" and scrape data
        # Use ".mem-item" - have to include . before class name
        #.select = soup method
    for member_card in soup.select(".mem-item"):
        # Pull name info - located in .mem-item class
        name_tag = member_card.select_one("h3 a") # target the parent element that has all desired info h3 and then target a w/in the h3 b/c that is where the name is - NO COMMA B/W ELEMENTS
        if name_tag: # if the member has a name
            name = name_tag.get_text(strip=True) # gets the text from the HTML element (the person's name), # strip=True removes whitespace (optional)
            profile_url = "https://nyassembly.gov" + name_tag["href"]  # pulls the member profile - it's the website url + the link savedin href (/mem/MembersName)
        else:
            continue # python keyword to make sure it moves on and doesn't get stuck
        
        # Pull address info - located in .mem-address class
        address_tag = member_card.select_one(".mem-address")
        if address_tag:
            address = address_tag.get_text(strip=True) #extracts the text from tag & removes leading spaces
        else:
            address = "No address listed"

        # Pull email info - located in .mem-email class
        email_tag = member_card.select_one(".mem-email") 
        if email_tag:
            email = email_tag.get_text(strip=True) # Extracts the text from the tag and removes any leading/trailing whitespaces
        else:
            email = "No email info available"

        #Pull social media info - located in .social-wrapper
        social_media_tag = member_card.select_one(".social-wrapper")
        if social_media_tag:
            social_media = social_media_tag.get_text(strip=True)
        else:
            social_media = "No social media info available"

        #Pull member photo link - located in .mem-pic class 
        picture_tag = member_card.select_one(".mem-pic")
        if picture_tag:
            picture = picture_tag.get_text(strip=True)
        else:
            picture = "No picture available"


        #STEP 6 - CREATE DICTIONARY
            # need to add assembly members name, profile, address, email, social media, & pic to the empty list members=[]
            # use dictionary - use ({})
            # Make sure that indentation is within the for loop
            # Add all information that you pulled in the rows above to this library
        members.append({"name": name, "profile_url": profile_url, "address": address, "email": email, "social_media": social_media, "picture": picture}) #appends all info taken above to this dictionary

    # STEP 7 - RETURN THE LIST OF RESULTS
    return members # lets you use the empty list somewhere else in the code


# STEP 8 - CREATE NEW FUNCTION TO SAVE LIST TO CSV
def save_to_csv(members, filename="ny_assembly_members.csv"):
    # use with open() - csv library commands - to create csv
    # mode="w" means write info in this file 
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        # Use csv library writer to write info in headers/rows 
        writer = csv.DictWriter(file, fieldnames=["name", "profile_url", "address", "email", "social_media", "picture"]) # field names must match the ones in the members.append dictionary
        # Write the headers & rows - rows should return the list
        writer.writeheader()
        writer.writerows(members)


# STEP 9 - EXECUTE SINGLE SCRIPT
if __name__ == "__main__":  # this is specific python code needed
    assembly_members = get_ny_assembly_members()  # set assembly members var = to the function b/c the function's job is to return the member info - must use () to invoke the function
    for member in assembly_members: # for each item in list of assembly members
        print(member) # print the info on the member
    save_to_csv(assembly_members) # call the save_to_csv function and give it the assembly members variable
