import sys
from datetime import datetime


# Takes string value and attempts to
# strip percentage and convert to float
def convertPercentToFloat(passedValue):
    # Try catch block, attempt to convert passed value to float, if it fails throw exception
    try:
        return float(passedValue.strip('%'))

    except Exception as e:
        print("Error: Converting passed percentage string: " + passedValue + " to float failed.\n", e)
        sys.exit()


# Takes string date as Day Month Year and return date object
def convertDateStringToDate(passedDateStr):
    # Try catch block, attempt to convert passed value to date, if it fails throw exception
    try:
        return datetime.strptime(passedDateStr, '%d %B %Y').date()

    except Exception as e:
        print("Error: Converting passed date string: " + passedDateStr + " to date failed.\n", e)
        sys.exit()


# Takes string paragraph and splits it into an array of strings, split on newline
def splitStringOnNewLine(passedParagraph):
    # Try catch block, attempt to split passed string on newlines, if it fails throw exception
    try:
        return passedParagraph.splitlines()

    except Exception as e:
        print("Error: Splitting passed string: " + passedParagraph + " by newlines failed.\n", e)
        sys.exit()
