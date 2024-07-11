# 	• Part 1 start/end time
# 		○ y-m-d, hour:min:sec
# 	• Part 2 start datae/start time
# 		○ Part 2 start date = y-m-d
# 		○ Part 2 start time = h:m:s
# 	• Part 2 end time
# 		○ Non-standard format



# To parse dates in standard format
# 	• Create list of col names
# 	• Use parse_dates argument and pass that list through
# 	• Then check the dtype of the time stamps columns
# 		○ In ex below, part 1 start & part 1 end are parsed successfully


# To parse split up time stamp columns
# 	• Add list w/in list w/ part 2 start date & part 2 start time
# 	• Pandas creates combined date/time col


# 	• To control col names, create/pass in a dictionary instead of the lists

# Non-standard dates
# 	• Parse_dates() doesn't work - will convert them to strings
# 	• Use pd.to_datetime() after loading


# 	• Strftime.org - is good resource
# 	• Below are the most important for formatting
# 		○ %Y
# 		○ %m
# 		○ %d
# 		○ %H
# 		○ %M
# 		○ %S

# Parsing part 2 end time w/ pd.to_datetime()


###EXERCISE 1 - PARSE SIMPLE DATES
# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=['Part1StartTime'])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())

# 0   2016-03-29 21:23:13
# 1   2016-03-29 21:24:59
# 2   2016-03-29 21:25:37
# 3   2016-03-29 21:21:37
# 4   2016-03-29 21:26:22
# Name: Part1StartTime, dtype: datetime64[ns]




##EXERCISE 2 - GET DATETIMES FROM MULTIPLE COLUMNS
# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ["Part2StartDate", "Part2StartTime"]}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates=datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())

#  count                    1000
#     unique                    985
#     top       2016-03-30 07:27:25
#     freq                        2
#     first     2016-03-29 21:24:57
#     last      2016-03-30 09:08:18
#     Name: Part2Start, dtype: object




##EXERCISE 4 - PARSE NON-STANDARD DATES
format_string = "%m%d%Y %H:%M:%S"

# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
                                  format=format_string)


