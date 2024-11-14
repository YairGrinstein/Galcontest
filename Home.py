from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.issta.co.il")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
driver.maximize_window()
# Accept cookies if prompted
try:
    accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "accept-cookies")))
    accept_cookies.click()
except:
    pass  # Skip if the cookie prompt doesn't appear

# Click on the "טיסות לחו"ל " tab
flight_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#wrapper > header > div.header-container.shell > nav > div > div > ul > li:nth-child(2) > a')))
flight_tab.click()
action = ActionChains(driver)
action.move_by_offset(0, 100).perform()

# Enter departure city (e.g., "תל אביב")
from_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/app-search-engine/div/se-group/div[1]/div[1]/div/se-tabs/div/se-tab/div/div/se-flights/se-flights-container/div/div[2]/div[1]/se-flights-form/form/div[1]/div[1]/div/div[1]/div/div[2]/se-flights-autocomplete/input')))
from_input.click()
from_input.send_keys("תל אביב")
time.sleep(1)  # Wait briefly for suggestions to load
#from_input.send_keys(Keys.RETURN)  # Select the first suggestion

# Enter destination city (e.g., "בודפשט")
to_input = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/app-search-engine/div/se-group/div[1]/div[1]/div/se-tabs/div/se-tab/div/div/se-flights/se-flights-container/div/div[2]/div[1]/se-flights-form/form/div[1]/div[1]/div/div[2]/div/div[2]/se-flights-autocomplete/input')))
to_input.click()
to_input.send_keys("בודפשט")
time.sleep(1)  # Wait briefly for suggestions to load
#to_input.send_keys(Keys.RETURN)  # Select the first suggestion

# Select departure date
departure_date = wait.until(EC.element_to_be_clickable((By.ID, 'start_date')))
departure_date.click()
select_departure_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="datepicker_widget"]/div/div[2]/table[2]/tbody/tr[5]/td[1]/div/span')))
select_departure_date.click()

# Select return date
return_date = wait.until(EC.element_to_be_clickable((By.ID, 'end_date')))
select_return_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="datepicker_widget"]/div/div[2]/table[2]/tbody/tr[2]/td[5]/div/span')))  # Adjust selector if needed
select_return_date.click()
select_return_date.send_keys(Keys.RETURN)

# Click the search button
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flights_form_a9d6db9c-1579-4c93-88ed-3b304649e5c4"]/div[1]/div[3]/div/form-button/button')))
search_button.click()


time.sleep(5)  #  wait for the results to load

# Select flights from search results

# Select the flight details (assuming it’s the first result)
departure_flight = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="all-flights-tab"]/section/div[3]/div[1]/div/section[2]/div/div[3]/a')))
departure_flight.click()

time.sleep(5)  #  wait for the page to load

# Proceed to Ordering details
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/main/div[2]/div/issta-branded-fares/issta-branded-fares-footer/div/div[2]/div/form/button')))
continue_button.click()

# Enter Person ordering information
first_name = wait.until(EC.visibility_of_element_located((By.ID, 'checkout-first-name')))
first_name.send_keys("ישראל")

last_name = wait.until(EC.visibility_of_element_located((By.ID, 'checkout-last-name')))
last_name.send_keys("ישראלי")

email_address = wait.until(EC.visibility_of_element_located((By.ID, 'checkout-email')))
email_address.send_keys("mail@mail.com")

phone_number = wait.until(EC.visibility_of_element_located((By.ID, 'checkout-phone')))
phone_number.send_keys("0505050505")


continue_details_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="customer_info_form"]/div[2]/button')))
continue_details_button.click()

time.sleep(5)  #  wait for the page to load

# Enter Passenger information
first_name = wait.until(EC.visibility_of_element_located((By.ID, 'PassengerDetailsVM.PassengersVM.Passengers[0].FirstName')))
first_name.send_keys("Israel")

last_name = wait.until(EC.visibility_of_element_located((By.ID, 'PassengerDetailsVM.PassengersVM.Passengers[0].LastName')))
last_name.send_keys("Israeli")

#gender list
gender_list = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="presonalDetailsForm"]/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[2]/span')))
gender_list.click()

gender_choose = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="presonalDetailsForm"]/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/ul/li[2]')))
gender_choose.click()

passport_number = wait.until(EC.visibility_of_element_located((By.ID, 'PassengerDetailsVM.PassengersVM.Passengers[0].Birthdate')))
passport_number.send_keys("123456789")

# Date of birth
dob = wait.until(EC.visibility_of_element_located((By.ID, 'PassengerDetailsVM.PassengersVM.Passengers[0].Birthdate')))
dob.send_keys("01011970")

#departure flight baggage
departure_flight_baggage = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="presonalDetailsForm"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[4]/div[2]/div[1]/div[1]/div[1]/i')))
departure_flight_baggage.click()

#return flight baggage
return_flight_baggage = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="presonalDetailsForm"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[9]/div[2]/div/div[2]/div[3]')))
return_flight_baggage.click()

#Proceed to payment page
checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="presonalDetailsForm"]/div[2]/button')))
checkout_button.click()
# Wait for results to load (this wait time may need adjusting)
time.sleep(5)  # Or use explicit wait for specific elements to load

# Close the driver after the task
driver.quit()
