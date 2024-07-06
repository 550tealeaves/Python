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




####SELECTING COLUMNS FROM SQL
# Create database engine for data.db
engine = create_engine("sqlite:///data.db")

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

# Make a dataframe by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)

# View the resulting dataframe
print(temperatures)

#            date  tmax  tmin
# 0    12/01/2017    52    42
# 1    12/02/2017    48    39
# 2    12/03/2017    48    42
# 3    12/04/2017    51    40
# 4    12/05/2017    61    50
# ..          ...   ...   ...
# 116  03/27/2018    47    34
# 117  03/28/2018    52    38
# 118  03/29/2018    53    49
# 119  03/30/2018    62    44
# 120  03/31/2018    58    39

# [121 rows x 3 columns]



##SELECTING ROWS
# Create query to get hpd311calls records about safety
query = """
SELECT *
FROM hpd311calls
WHERE complaint_type = 'SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()




##FILTERING ON MULTIPLE CONDITIONS
# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32
  OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())

#         latitude  longitude  elevation    awnd    prcp    snow    tmax    tmin
# count  2.500e+01  2.500e+01  2.500e+01  25.000  25.000  25.000  25.000  25.000
# mean   4.078e+01 -7.397e+01  4.270e+01   7.740   0.176   1.332  27.320  17.160
# std    7.252e-15  1.450e-14  7.252e-15   2.622   0.369   2.685   7.122   7.674
# min    4.078e+01 -7.397e+01  4.270e+01   3.130   0.000   0.000  13.000   5.000
# 25%    4.078e+01 -7.397e+01  4.270e+01   5.820   0.000   0.000  22.000  11.000
# 50%    4.078e+01 -7.397e+01  4.270e+01   7.830   0.000   0.000  28.000  17.000
# 75%    4.078e+01 -7.397e+01  4.270e+01   9.170   0.090   1.200  31.000  20.000
# max    4.078e+01 -7.397e+01  4.270e+01  12.970   1.410   9.800  40.000  33.000