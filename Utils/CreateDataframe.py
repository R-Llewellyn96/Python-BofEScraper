import sys
import pandas as pd


# Create Dataframe from passed list object
def fromList(passedList):
    # Try catch block, attempt to insert values to dictionary, if it fails throw exception
    try:
        # Put list of data into a dataframe,
        # for easy upload to SQL database
        return pd.DataFrame(passedList)
    except Exception as e:
        print("Error: Converting passed List to Dataframe failed.\n", e)
        sys.exit()


# Convert dataframe field to date
def convertDfFieldToDate(passedDf):
    # Try catch block, attempt to convert field to date, if it fails throw exception
    try:
        # Convert field string to date format
        passedDf['next_update'] = pd.to_datetime(passedDf['next_update'], dayfirst=True).dt.date
        return passedDf
    except Exception as e:
        print("Error: Converting field string: " + passedDf + "  to date failed.\n", e)
        sys.exit()
