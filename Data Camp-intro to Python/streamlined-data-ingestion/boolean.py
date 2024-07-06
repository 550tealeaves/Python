# 	• Dataset has
# 		○ ID col
# 		○ Col on if attended bootcamp (y/n) + boolean
# 		○ Col on if they took out loan (y/n) + boolean


# 	• Col w/ boolean values not typed as boolean, were typed as float
# 	• Why?


# 	• 38 attended bootcamp, 14 took out loan

# 	• Sum total missing values with .isna().sum()
# 		○ No missing for bootcamp
# 		○ But plenty missing data for loans


# 	• To convert the data type of boolean columns to boolean, 
# 		○ Use dtype and pass dictionary that specifies which col are boolean


# 	• But when you check the sum of trues afterwords, there are still issues
# 		○ Loan col has too many trues
# 	• Check missing value - .isna() - no missing 


# 	• What happened?
# 		○ Pandas loads T/F col as floats by default
# 		○ Use dtype to in read_excel() argument to change cols to bool
# 		○ Since booleans must have T or F, it recodes NA's as True = problem
# 			§ Pandas knows that 1=True, and 0=False, but doesn't know that yes=True and no=False

# SOLUTION
# 	• Use read_excel() - true_values() argument & set custom True values
# 	• Use read_excel() - false_values() argument & set custom False values
# 	• Arguments take a list of values that are treated as True or False

# 	• Pass the single list item of yes/no to true_values/false_values, respectively

# 	• 

# 	• Check True counts w/ .sum() method
# 	• Problem is that NA's are still recoded as True




##EXERCISE 1 - SET BOOLEAN COLS
# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx", dtype=())

# Count NA values in each column
print(survey_data.isna().sum())



##EXERCISE 2 - SET BOOLEAN COLUMNS
# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype={"HasDebt": bool})

# View financial burdens by Boolean group
print(survey_data.groupby("HasDebt").sum())


#          HasFinancialDependents  HasHomeMortgage  HasStudentDebt
# HasDebt                                                         
# False                     112.0              0.0             0.0
# True                      205.0            151.0           281.0




##CUSTOM T/F VALUES
# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values=["Yes"],
                              false_values=["No"])

# View the data
print(survey_subset.head())


#                                ID.x  AttendedBootCampYesNo  HasDebt  HasFinancialDependents  HasHomeMortgage  HasStudentDebt
# 0  cef35615d61b202f1dc794ef2746df14                  False     True                     1.0              0.0             1.0
# 1  323e5a113644d18185c743c241407754                  False    False                     0.0              NaN             NaN
# 2  b29a1027e5cd062e654a63764157461d                  False    False                     0.0              NaN             NaN
# 3  04a11e4bcb573a1261eb0d9948d32637                  False     True                     0.0              0.0             1.0
# 4  9368291c93d5d5f5c8cdb1a575e18bec                  False     True                     0.0              0.0             0.0