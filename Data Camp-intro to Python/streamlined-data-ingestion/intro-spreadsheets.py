
# 	• Pandas uploads basic files w/ no formatting


# 	• Use read_excel() to load spreadsheet to Python


# 	• What makes spreadsheets complicated is they can have non-tabular data, such as
# 		○ Metadata headers
# 		○ Smaller tables of info
# 	• But read_excel() has arguments to select cols or skip them 

# Loading select cols/rows - diff in arguments b/w read_excel()  &read_csv()
# 	• Nrows & skiprows = same
# 	• Usecols - a bit diff from read_csv()
# 		○ Accepts integer of cols to load
# 		○ Accepts string of excel col letters or ranges

	
# 	• Data on jobs from cols W-AB
# 	• Data on income from AR
# 	• 2 row header with source info that will be excluded


# 	• Skiprows=2
# 		○ Excludes metadata
# 	• Usecols="W:AB, AR"
# 		○ Only imports those select cols



## EXERCISE 1 - LOAD DATA FROM SPREADSHEET
# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("fcc_survey.xlsx")

# View the head of the dataframe
print(survey_responses.head())

#     Age  AttendedBootcamp  BootcampFinish  BootcampLoanYesNo BootcampName  ...  ResourceUdemy  ResourceW3Schools                             SchoolDegree              SchoolMajor  StudentDebtOwe
# 0  28.0               0.0             NaN                NaN          NaN  ...            NaN                NaN           some college credit, no degree                      NaN           20000
# 1  22.0               0.0             NaN                NaN          NaN  ...            1.0                NaN           some college credit, no degree                      NaN             NaN
# 2  19.0               0.0             NaN                NaN          NaN  ...            NaN                NaN  high school diploma or equivalent (GED)                      NaN             NaN
# 3  26.0               0.0             NaN                NaN          NaN  ...            NaN                NaN                        bachelor's degree  Cinematography And Film            7000
# 4  20.0               0.0             NaN                NaN          NaN  ...            NaN                NaN           some college credit, no degree                      NaN             NaN




## EXERCISE 2 - LOAD PORTION OF SPREADSHEET
# Create string of lettered columns to load
col_string = "AD, AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        skiprows=2, 
                        usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)


# Index(['ExpectedEarning', 'JobApplyWhen', 'JobPref', 'JobRelocateYesNo', 'JobRoleInterest', 'JobWherePref'], dtype='object')




####### LOADING DATA FROM MULTIPLE SPREADSHEETS ####

# LOADING DATA FROM MULTIPLE SPREADSHEETS

# 	• Sheets are 0 index
# 	• If you load multiple sheets, any argument in read_excel() will apply to all of them
# 	• If sheets need diff parameters, load them w/ separate read_excel() calls


# 	• 2016 sheet will load by default b/c it's first


# 	• Use either position index or name to load

# Loading all sheets
# 	• Pass sheet_name=None to read_excel() and it will load all sheets

# 	• Ex above shows that the type for ALL the sheets loaded = ordered dictionary
# 	• Iterate through items shows 
# 		○ Keys = sheet names 
# 		○ Values = DataFrames for each sheet'

# Loading multiple sheets w/ same cols into 1 dataframe
# 	• Diff dataframes make sense if you have diff cols or subjects
# 	• But if sheets have same col but diff year, can combine them into 1 dataframe

# 	1. Create empty dataframe
# 		a. All_responses = pd.DataFrame()
# 	2. Loop through (iterate) through items in survey responses dictionary 
# 		a. Each value = dataframe corresponding to each worksheet
# 		b. Keys = sheet names 
# 		c. For each dataframe add a "Year" col that has the sheet name
# 	3. Add dataframe to all responses by passing list of dataframes to combine to the pd.concat function
# 	4. Check unique values in "Year" col
# 		a. Confirms that all responses have both years




##EXERCISE 1 - SELECT 1 SHEET
# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name="2017")

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()


## EXERCISE 2 - LOAD MULTIPLE SHEETS
# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=['2016', '2017']) #passes list of sheet names

# View the data type of all_survey_data
print(type(all_survey_data))

# <class 'dict'>


##EXERCISE 3 - LOAD MULTIPLE SHEETS - BY POSITION NUMBER
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=[0,'2017']) #lists first sheet(index=0) & 2nd sheet by name as string

# View the sheet names in all_survey_data
print(all_survey_data.keys())

# dict_keys([0, '2017'])



##EXERCISE 4 - LOAD MULTIPLE SHEETS - W/O NAMING ANY
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())




##EXERCISE 5 - WORK W/ MULTIPLE SPREADSHEETS
# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Concatenate all_responses and df, assign result
  all_responses = pd.concat([all_responses, df])

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()


# Adding 1000 rows
# Adding 1000 rows
