from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import Utils.StringToValueConverter
import Utils.ValuesToBofEDict
import Utils.CreateDataframe


# Bypass popups and go to main site
def bypassPopup(url_to_get):

    # Go to passed URL
    driver.get(url_to_get)

    # Implicit wait for webpage
    driver.implicitly_wait(5)

    # Get xpath to cookie accept popup button
    cookie_popup_button_xpath = '/html/body/div[1]/div[1]/div/div/table/tbody/tr[2]/td[3]/button'

    # Wait of JS page elements to load
    WebDriverWait(driver, 30).until(ec.element_to_be_clickable(
        (By.XPATH, cookie_popup_button_xpath)))

    # Click consent button to accept and go to url we want
    driver.find_element_by_xpath(cookie_popup_button_xpath).click()


# Main Method, calls functions
if __name__ == '__main__':

    # URL to search
    URL = 'https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate'

    # Define browser options
    options = Options()

    # Dont render to a GUI (Cant be used on anti-scraping sites)
    options.headless = True

    # Set headless window size to maximise rendering
    options.add_argument('window-size=2160x3840')

    # Setup webdriver, running in headless mode
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Get webpage from URL
    bypassPopup(URL)

    # Get the featured stat box, so we can grab the elements it contains
    base_rate_box = driver.find_element_by_class_name("featured-stat")

    # Get title of base_rate_box
    base_rate_title = base_rate_box.find_element_by_tag_name('h2').text

    # Get base rate from base_rate_box
    base_rate_value = base_rate_box.find_element_by_tag_name('span').text

    # Get date of next update to base rate
    base_rate_update = base_rate_box.find_element_by_tag_name('p').text

    # Kill browser instance
    driver.close()

    # List to store the dictionary we will make,
    # this gives our dictionary input an index value
    results_list = []

    # Cut next line from base_rate_title, grab first array element as title
    base_rate_title = Utils.StringToValueConverter.splitStringOnNewLine(base_rate_title)[0]

    # Cut all text except value from base_rate_value
    base_rate_value = Utils.StringToValueConverter.convertPercentToFloat(base_rate_value)

    # Cut all text except date from date
    base_rate_update = Utils.StringToValueConverter.convertDateStringToDate(base_rate_update.strip('Next due: '))

    # Convert date to String for adding to dataframe
    base_rate_update = base_rate_update.strftime('%Y-%m-%d')

    # Create dictionary to store values and allow conversion to dataframe, args: title, value, update date
    dictToConvert = Utils.ValuesToBofEDict.addValuesToBofEDict(base_rate_title, base_rate_value, base_rate_update)

    # Add our created dictionary to the results list
    results_list.append(dictToConvert)

    # Put list of data into a dataframe,
    # for easy upload to SQL database
    df = Utils.CreateDataframe.fromList(results_list)

    # Convert string date to date object in dataframe
    dfWithDate = Utils.CreateDataframe.convertDfFieldToDate(df)

    # Tell user dataframe gathered
    print("\nGathered Data\n")

    # Print dataframe
    print(df)
