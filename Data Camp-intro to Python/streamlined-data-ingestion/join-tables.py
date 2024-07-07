##EXERCISE 1 - JOIN TABLES

# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create dataframe of joined tables
calls_with_weather = pd.read_sql(query, engine)

# View the dataframe to make sure all columns were joined
print(calls_with_weather.head())

#   unique_key created_date agency  complaint_type incident_zip  ... prcp snow tavg tmax tmin
# 0   38070822   01/01/2018    HPD  HEAT/HOT WATER        10468  ...  0.0  0.0        19    7
# 1   38065299   01/01/2018    HPD        PLUMBING        10003  ...  0.0  0.0        19    7
# 2   38066653   01/01/2018    HPD  HEAT/HOT WATER        10452  ...  0.0  0.0        19    7
# 3   38070264   01/01/2018    HPD  HEAT/HOT WATER        10032  ...  0.0  0.0        19    7
# 4   38072466   01/01/2018    HPD  HEAT/HOT WATER        11213  ...  0.0  0.0        19    7

# [5 rows x 21 columns]



##EXERCISE 2 - JOINING & FILTERING
# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date;"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())

#   unique_key created_date agency  complaint_type incident_zip      incident_address community_board    borough  prcp
# 0   38070822   01/01/2018    HPD  HEAT/HOT WATER        10468    2786 JEROME AVENUE        07 BRONX      BRONX   0.0
# 1   38065299   01/01/2018    HPD        PLUMBING        10003  323 EAST   12 STREET    03 MANHATTAN  MANHATTAN   0.0
# 2   38066653   01/01/2018    HPD  HEAT/HOT WATER        10452  1235 GRAND CONCOURSE        04 BRONX      BRONX   0.0
# 3   38070264   01/01/2018    HPD  HEAT/HOT WATER        10032  656 WEST  171 STREET    12 MANHATTAN  MANHATTAN   0.0
# 4   38072466   01/01/2018    HPD  HEAT/HOT WATER        11213       1030 PARK PLACE     08 BROOKLYN   BROOKLYN   0.0



# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())

#   unique_key created_date agency complaint_type incident_zip         incident_address community_board   borough  prcp
# 0   38074305   01/01/2018    HPD     WATER LEAK        11212     1026 WILLMOHR STREET     17 BROOKLYN  BROOKLYN   0.0
# 1   38078748   01/01/2018    HPD     WATER LEAK        10458       2700 MARION AVENUE        07 BRONX     BRONX   0.0
# 2   38081097   01/01/2018    HPD     WATER LEAK        11221  192 MALCOLM X BOULEVARD     03 BROOKLYN  BROOKLYN   0.0
# 3   38077874   01/01/2018    HPD     WATER LEAK        11418    129-11 JAMAICA AVENUE       09 QUEENS    QUEENS   0.0
# 4   38081110   01/01/2018    HPD     WATER LEAK        11420        111-17 133 STREET       10 QUEENS    QUEENS   0.0




##JOINING, FILTERING, AGGREGATING
# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())

#   created_date  COUNT(*)
# 0   01/01/2018      4597
# 1   01/02/2018      4362
# 2   01/03/2018      3045
# 3   01/04/2018      3374
# 4   01/05/2018      4333





# Modify query to join tmax and tmin from weather by date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*), 
       weather.tmax, 
       weather.tmin
  FROM hpd311calls 
       JOIN weather 
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
 """

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())

#   created_date  COUNT(*)  tmax  tmin
# 0   01/01/2018      4597    19     7
# 1   01/02/2018      4362    26    13
# 2   01/03/2018      3045    30    16
# 3   01/04/2018      3374    29    19
# 4   01/05/2018      4333    19     9