##  EXERCISE 1 - LOAD DATA
# Load pandas as pd
import pandas as pd

# Load the daily report to a dataframe
pop_in_shelters = pd.read_json('dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())

#        adult_families_in_shelter  adults_in_families_with_children_in_shelter  children_in_families_with_children_in_shelter  families_with_children_in_shelter  \
# count                   1000.000                                     1000.000                                       1000.000                           1000.000   
# mean                    2074.955                                    16487.932                                      23273.873                          11588.835   
# std                      148.020                                      848.364                                        926.244                            626.414   
# min                     1796.000                                    14607.000                                      21291.000                          10261.000   
# 25%                     1906.000                                    15831.500                                      22666.000                          11060.000   
# 50%                     2129.000                                    16836.000                                      23285.500                          11743.000   
# 75%                     2172.250                                    17118.250                                      23610.000                          12146.000   
# max                     2356.000                                    17733.000                                      25490.000                          12413.000   

#        individuals_in_adult_families_in_shelter  ...  total_adults_in_shelter  total_children_in_shelter  total_individuals_in_families_with_children_in_shelter_  total_individuals_in_shelter  \
# count                                  1000.000  ...                 1000.000                   1000.000                                           1000.000                            1000.000   
# mean                                   4368.054  ...                32328.857                  23273.882                                          39761.805                           55602.739   
# std                                     299.054  ...                 2150.584                    926.247                                           1677.973                            2745.294   
# min                                    3811.000  ...                28127.000                  21291.000                                          35902.000                           49462.000   
# 25%                                    4026.000  ...                30184.250                  22666.000                                          38775.500                           53196.500   
# 50%                                    4473.000  ...                33142.000                  23285.500                                          40026.000                           56713.500   
# 75%                                    4567.000  ...                33940.750                  23610.000                                          40529.500                           57872.250   
# max                                    4944.000  ...                35294.000                  25490.000                                          43208.000                           59068.000   

#        total_single_adults_in_shelter  
# count                        1000.000  
# mean                        11472.880  
# std                          1113.664  
# min                          9610.000  
# 25%                         10381.750  
# 50%                         11633.500  
# 75%                         12437.500  
# max                         13270.000  

# [8 rows x 12 columns]



##EXERCISE 2 - WORK W/ JSON ORIENTATIONS
try:
    # Load the JSON without keyword arguments
    df = pd.read_json("dhs_report_reformatted.json")
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")












api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                        headers=headers, 
                        params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a dataframe
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)


# id                object
# alias             object
# name              object
# image_url         object
# is_closed           bool
# url               object
# review_count       int64
# categories        object
# rating           float64
# coordinates       object
# transactions      object
# location          object
# phone             object
# display_phone     object
# distance         float64
# price             object
# dtype: object



##EXERCISE 2 - SET API PARAMETERS
# Create dictionary to query API for cafes in NYC
parameters = {"term": "cafe",
          	  "location": "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url, 
                        headers=headers, 
                        params=parameters)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())

#           phone   display_phone  distance price  
# 0                                1856.127   NaN  
# 1  +17182856180  (718) 285-6180  2087.817    $$  
# 2  +12122287888  (212) 228-7888  2435.843    $$  
# 3  +16465246353  (646) 524-6353  1657.233     $  
# 4  +17188018037  (718) 801-8037   635.782    $$  

# [5 rows x 16 columns]




##SET REQUEST HEADERS
# Create dictionary that passes Authorization and key string
headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url, 
                        headers=headers, 
                        params=params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)


# 0             Coffee Project NY
# 1                Urban Backyard
# 2              Saltwater Coffee
# 3                 Bird & Branch
# 4                  Bibble & Sip
# 5             Coffee Project NY
# 6                        Burrow
# 7                   Cafe Patoro
# 8                     Sweatshop
# 9                       Round K
# 10               Kobrick Coffee
# 11            Kaigo Coffee Room
# 12              Absolute Coffee
# 13                     Devocion
# 14                The Uncommons
# 15                      Butler 
# 16              Cafe Hanamizuki
# 17    Brooklyn Roasting Company
# 18             Takahachi Bakery
# 19              Happy Bones NYC
# Name: name, dtype: object













# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
                       sep="_")

# View data
print(cafes.head())

#                   location_display_address price  
# 0        [71 Smith St, Brooklyn, NY 11201]   NaN  
# 1  [276 Livingston St, Brooklyn, NY 11201]    $$  
# 2       [239 E 5th St, New York, NY 10003]    $$  
# 3     [116 Suffolk St, New York, NY 10002]     $  
# 4       [163 Plymouth St, Dumbo, NY 11201]    $$  

# [5 rows x 24 columns]










# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                            sep="_")

# View the data
print(flat_cafes.head())

#                  location_display_address price  
# 0        [71 Smith St, Brooklyn, NY 11201]   NaN  
# 1  [276 Livingston St, Brooklyn, NY 11201]    $$  
# 2       [239 E 5th St, New York, NY 10003]    $$  
# 3     [116 Suffolk St, New York, NY 10002]     $  
# 4       [163 Plymouth St, Dumbo, NY 11201]    $$  

# [5 rows x 24 columns]









# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories")

# View the data
print(flat_cafes.head())

#               alias              title
# 0            coffee       Coffee & Tea
# 1            coffee       Coffee & Tea
# 2  coffeeroasteries  Coffee Roasteries
# 3             cafes              Cafes
# 4            coffee       Coffee & Tea










# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=["name", 
                                  "alias",  
                                  "rating",
                          		  ["coordinates", "latitude"], 
                          		  ["coordinates", "longitude"]],
                    		meta_prefix="biz_")

# View the data
print(flat_cafes.head())

#               alias              title           biz_name                   biz_alias biz_rating biz_coordinates_latitude biz_coordinates_longitude
# 0            coffee       Coffee & Tea        White Noise      white-noise-brooklyn-2        4.5                   40.689                   -73.988
# 1            coffee       Coffee & Tea           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
# 2  coffeeroasteries  Coffee Roasteries           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
# 3             cafes              Cafes           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
# 4            coffee       Coffee & Tea  Coffee Project NY  coffee-project-ny-new-york        4.5











