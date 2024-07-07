##EX 1 - CONCATENATE DATAFRAMES
# Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])
# Concatenate the results, setting ignore_index to renumber rows
cafes = pd.concat([top_50_cafes, next_50_cafes], ignore_index=True)

# Print shape of cafes
print(cafes.shape) #(100, 24)




##EX 2 - MERGE DATAFRAMES

# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, 
                   			   left_on="location_zip_code", 
                               right_on="zipcode")

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on="puma")

# View the data
print(cafes_with_pop.head())


#                         alias                                         categories  coordinates_latitude  coordinates_longitude   display_phone  ...  geo_type  \
# 0  coffee-project-ny-new-york     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]                40.727                -73.989  (212) 228-7888  ...  PUMA2010   
# 1   saltwater-coffee-new-york     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]                40.730                -73.984  (917) 881-2245  ...  PUMA2010   
# 2   daily-provisions-new-york  [{'alias': 'cafes', 'title': 'Cafes'}, {'alias...                40.738                -73.988  (212) 488-1505  ...  PUMA2010   
# 3              mud-new-york-3  [{'alias': 'coffee', 'title': 'Coffee & Tea'},...                40.729                -73.987  (212) 228-9074  ...  PUMA2010   
# 4  coffee-project-ny-new-york     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]                40.727                -73.989  (212) 228-7888  ...  PUMA2010   

#                                            geog_name    borough  total_pop_estimate total_pop_moe  
# 0  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
# 1  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
# 2  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
# 3  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
# 4  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  

# [5 rows x 37 columns]