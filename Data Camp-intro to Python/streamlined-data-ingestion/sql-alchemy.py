# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine 



##CONNECT TO DATABASE
# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("sqlite:///data.db")

# View the tables in the database
print(engine.table_names())




##LOAD ENTIRE TABLES
# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("sqlite:///data.db")

# View the tables in the database
print(engine.table_names())

#   unique_key created_date agency  complaint_type incident_zip      incident_address community_board    borough
# 0   38070822   01/01/2018    HPD  HEAT/HOT WATER        10468    2786 JEROME AVENUE        07 BRONX      BRONX
# 1   38065299   01/01/2018    HPD        PLUMBING        10003  323 EAST   12 STREET    03 MANHATTAN  MANHATTAN
# 2   38066653   01/01/2018    HPD  HEAT/HOT WATER        10452  1235 GRAND CONCOURSE        04 BRONX      BRONX
# 3   38070264   01/01/2018    HPD  HEAT/HOT WATER        10032  656 WEST  171 STREET    12 MANHATTAN  MANHATTAN
# 4   38072466   01/01/2018    HPD  HEAT/HOT WATER        11213       1030 PARK PLACE     08 BROOKLYN   BROOKLYN



##LOAD ENTIRE TABLES


# Create the database engine
engine = create_engine("sqlite:///data.db")

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""

# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())


#        station                         name  latitude  longitude  elevation  ...  prcp snow  tavg  tmax  tmin
# 0  USW00094728  NY CITY CENTRAL PARK, NY US    40.779    -73.969       42.7  ...  0.00  0.0          52    42
# 1  USW00094728  NY CITY CENTRAL PARK, NY US    40.779    -73.969       42.7  ...  0.00  0.0          48    39
# 2  USW00094728  NY CITY CENTRAL PARK, NY US    40.779    -73.969       42.7  ...  0.00  0.0          48    42
# 3  USW00094728  NY CITY CENTRAL PARK, NY US    40.779    -73.969       42.7  ...  0.00  0.0          51    40
# 4  USW00094728  NY CITY CENTRAL PARK, NY US    40.779    -73.969       42.7  ...  0.75  0.0          61    50

# [5 rows x 13 columns]