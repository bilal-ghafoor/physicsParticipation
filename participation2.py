from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver service using webdriver-manager
service = Service(ChromeDriverManager().install())

# Create the Chrome driver with the service
driver = webdriver.Chrome(service=service)

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

# Input email and password
email = "your_email"
password = "your_password"

# Wait for the email input field to appear
email_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "username"))
)
email_input.send_keys(email)

# Wait for the password input field to appear
password_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_input.send_keys(password)

# Wait for the sign in button to appear
sign_in_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "mainButton"))
)
sign_in_button.click()

# Wait for the "Lecture 12 poll questions" link to appear
lecture_link = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[5]/div/div[5]/div[1]/div[3]/ul/li/a"))
)
lecture_link.click()

while True:
    try:
        # Wait for the multiple choice options to appear
        response_options = WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.response.multiplechoice"))
        )

        # Wait 2 seconds before clicking the option
        time.sleep(2)

        # Click on the first option
        response_options[0].click()
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
