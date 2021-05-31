import sys


# Takes input functions and adds to dictionary
def addValuesToBofEDict(title, rate, update):

    # Try catch block, attempt to insert values to dictionary, if it fails throw exception
    try:
        # Create dictionary to store values and allow conversion to dataframe
        bOfE_values_dict = {
            'title': title,
            'base_rate': rate,
            'next_update': update
        }
        return bOfE_values_dict

    except Exception as e:
        print("Error: Inserting passed values to dictionary failed.\n", e)
        sys.exit()
