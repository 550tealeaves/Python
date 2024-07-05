# 	• Typing out entry cell by cell is not most efficient way to convert to dataframe

# What is CSV?
# 	• Designed for DataFrame like data
# 	• Each row has its own line
# 	• Each value separated by comma
# 	• Very versatile and used for diff programs - also shareable


# 	• Use pd.read_csv("csv-file-name.csv") to convert CSV to dataframe
# 	• Since now Dataframe, can use functions learned earlier to manipulate it


# Convert DataFrame to CSV
# 	• Use .to_csv() method
# 		○ Pass in new file path



## EXERCISE 1

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")

# Take a look at the DataFrame
print(airline_bumping)

#                 airline  year  nb_bumped  total_passengers
# 0       DELTA AIR LINES  2017        679          99796155
# 1        VIRGIN AMERICA  2017        165           6090029
# 2       JETBLUE AIRWAYS  2017       1475          27255038
# 3       UNITED AIRLINES  2017       2067          70030765
# 4     HAWAIIAN AIRLINES  2017         92           8422734
# 5   EXPRESSJET AIRLINES  2017        785          11738812
# 6      SKYWEST AIRLINES  2017        917          24516354
# 7     AMERICAN AIRLINES  2017       4517          98017132
# 8       ALASKA AIRLINES  2017        658          18817924
# 9    SOUTHWEST AIRLINES  2017       6678         115988988
# 10    FRONTIER AIRLINES  2017        540          12059943
# 11      SPIRIT AIRLINES  2017       1502          17069647
# 12      DELTA AIR LINES  2016        912          97237060
# 13       VIRGIN AMERICA  2016         77           5927938
# 14      JETBLUE AIRWAYS  2016       2140          25990828
# 15      UNITED AIRLINES  2016       2874          64438132
# 16    HAWAIIAN AIRLINES  2016         30           8154838
# 17  EXPRESSJET AIRLINES  2016       2541          16119866
# 18     SKYWEST AIRLINES  2016       2177          22575383
# 19    AMERICAN AIRLINES  2016       6598          99348093
# 20      ALASKA AIRLINES  2016        734          17725197
# 21   SOUTHWEST AIRLINES  2016      11907         112153048
# 22    FRONTIER AIRLINES  2016        688          10895052
# 23      SPIRIT AIRLINES  2016       1418          15234924



#EXERCISE 2

# From previous step
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

    #          airline  year  nb_bumped  total_passengers
    # 0    DELTA AIR LINES  2017        679          99796155
    # 1     VIRGIN AMERICA  2017        165           6090029
    # 2    JETBLUE AIRWAYS  2017       1475          27255038
    # 3    UNITED AIRLINES  2017       2067          70030765
    # 4  HAWAIIAN AIRLINES  2017         92           8422734


##EXERCISE 3
# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

#              airline  year  nb_bumped  total_passengers
# 0    DELTA AIR LINES  2017        679          99796155
# 1     VIRGIN AMERICA  2017        165           6090029
# 2    JETBLUE AIRWAYS  2017       1475          27255038
# 3    UNITED AIRLINES  2017       2067          70030765
# 4  HAWAIIAN AIRLINES  2017         92           8422734



##EXERCISE 4
# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)


#              airline  year  nb_bumped  total_passengers
# 0    DELTA AIR LINES  2017        679          99796155
# 1     VIRGIN AMERICA  2017        165           6090029
# 2    JETBLUE AIRWAYS  2017       1475          27255038
# 3    UNITED AIRLINES  2017       2067          70030765
# 4  HAWAIIAN AIRLINES  2017         92           8422734
#                      nb_bumped  total_passengers  bumps_per_10k
# airline                                                        
# ALASKA AIRLINES           1392          36543121          0.381
# AMERICAN AIRLINES        11115         197365225          0.563
# DELTA AIR LINES           1591         197033215          0.081
# EXPRESSJET AIRLINES       3326          27858678          1.194
# FRONTIER AIRLINES         1228          22954995          0.535
# HAWAIIAN AIRLINES          122          16577572          0.074
# JETBLUE AIRWAYS           3615          53245866          0.679
# SKYWEST AIRLINES          3094          47091737          0.657
# SOUTHWEST AIRLINES       18585         228142036          0.815
# SPIRIT AIRLINES           2920          32304571          0.904
# UNITED AIRLINES           4941         134468897          0.367
# VIRGIN AMERICA             242          12017967          0.201



##EXERCISE 5
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")

#                      nb_bumped  total_passengers  bumps_per_10k
# airline                                                        
# EXPRESSJET AIRLINES       3326          27858678          1.194
# SPIRIT AIRLINES           2920          32304571          0.904
# SOUTHWEST AIRLINES       18585         228142036          0.815
# JETBLUE AIRWAYS           3615          53245866          0.679
# SKYWEST AIRLINES          3094          47091737          0.657
# AMERICAN AIRLINES        11115         197365225          0.563
# FRONTIER AIRLINES         1228          22954995          0.535
# ALASKA AIRLINES           1392          36543121          0.381
# UNITED AIRLINES           4941         134468897          0.367
# VIRGIN AMERICA             242          12017967          0.201
# DELTA AIR LINES           1591         197033215          0.081
# HAWAIIAN AIRLINES          122          16577572          0.074