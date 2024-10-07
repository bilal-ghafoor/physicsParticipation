from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Set up the Chrome driver service using webdriver-manager
service = Service(ChromeDriverManager().install())

# Create the Chrome driver with the service
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/YourUsername/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the LearningCatalytics website
driver.get("https://learningcatalytics.com/class_sessions/39002365")

# Wait 7 seconds before starting
time.sleep(7)

# Check if the "Allow and Continue" button is present and click it
try:
    allow_button = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )
    allow_button.click()
except:
    pass

# Check if the login form is present
try:
    email_input = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password_input = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    sign_in_button = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "mainButton"))
    )
    email = "bghafoor@gmu.edu"
    password = "Escape961A"
    email_input.send_keys(email)
    password_input.send_keys(password)
    sign_in_button.click()
except:
    pass

# Wait 2 seconds before continuing
time.sleep(2)

# Check if the "Lecture 12 poll questions" link is present and click it
try:
    lecture_link = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[5]/div/div[5]/div[1]/div[3]/ul/li/a"))
    )
    lecture_link.click()
except:
    pass

# Wait 2 seconds before continuing
time.sleep(2)

# Check if the "Allow and Continue" button is present again and click it
try:
    allow_button = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )
    allow_button.click()
except:
    pass

while True:
    try:
        # Wait for the multiple choice options to appear
        response_options = WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.response.multiplechoice"))
        )

        # Get the number of options
        num_options = len(response_options)

        # Generate a random number between 0 and the number of options
        random_num = random.randint(0, num_options - 1)

        # Click on the random option
        response_options[random_num].click()
    except:
        try:
            # Wait for the short answer input field to appear
            input_field = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[5]/div/div[5]/div[4]/form/input[2]"))
            )

            # Enter a response and press Enter
            input_field.send_keys("ability to do stuff")
            input("Press Enter to submit your response…")
        except:
            # If no question is found, wait for 1 second and try again
            print("No question found. Waiting for 1 second and trying again…")
            import time
            time.sleep(1)
