from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuring Chrome options to keep the browser open after the script completes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initializing the WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# URL of the Google Form
google_form_url = 'https://forms.gle/WT68aV5UnPajeoSc8'

try:
    # Opening the Google Form page
    driver.get(google_form_url)

    # Waiting for the form to load
    time.sleep(5)

    # Locating all text input fields in the form
    input_list = driver.find_elements(by=By.XPATH, value="//input[@type='text']")

    # Filling out the text input fields with sample data
    input_list[0].send_keys('Vansh Singh Chaudhary')
    input_list[1].send_keys('88888888')
    input_list[2].send_keys('abc@gmail.com')

    # Locating and filling the address field
    address_field = driver.find_element(by=By.XPATH, value="//textarea")
    address_field.send_keys('Village ABC Distt. XYZ ABC state')

    # Filling out additional input fields with sample data
    input_list[3].send_keys('111111')

    # Locating and setting the date in the date input field
    date_field = driver.find_element(By.XPATH, "//input[@type='date']")
    date_field.send_keys('2024-12-31')

    # Filling out the remaining input fields
    input_list[4].send_keys('Male')
    input_list[5].send_keys('GNFPYC')

    # Locating and clicking the submit button
    submit = driver.find_element(by=By.XPATH, value="//span[text()='Submit']")
    submit.click()

    # Taking a screenshot of the page after form submission
    screenshot_path = f"screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot taken successfully: {screenshot_path}")

except Exception as e:
    # Printing any errors encountered during the execution
    print(f"An error occurred: {e}")

finally:
    # Waiting for a few seconds before closing the browser (optional)
    time.sleep(10)

    # Closing the browser
    driver.quit()
