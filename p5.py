import tkinter as tk
from tkinter import messagebox
import os
import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LearningCatalyticsUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Learning Catalytics UI")

        self.headless_var = tk.BooleanVar()
        self.headless_var.set(False)

        self.email_label = tk.Label(self.window, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack()

        self.password_label = tk.Label(self.window, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        self.headless_checkbox = tk.Checkbutton(self.window, text="Headless mode", variable=self.headless_var)
        self.headless_checkbox.pack()

        self.start_button = tk.Button(self.window, text="Start", command=self.start_script)
        self.start_button.pack()

    def start_script(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        headless = self.headless_var.get()

        if email and password:
            self.window.destroy()
            self.run_script(email, password, headless)
        else:
            messagebox.showerror("Error", "Please enter email and password")

    def run_script(self, email, password, headless):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=" + os.path.join(os.path.expanduser("~"), "AppData", "Local", "Google", "Chrome", "User Data"))
        if headless:
            options.add_argument("--headless")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://learningcatalytics.com/class_sessions/39002365")

        time.sleep(7)

        while True:
            try:
                allow_button = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
                )
                allow_button.click()
            except:
                print("Failed to find 'Allow and Continue' button. Continuing...")

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
                email_input.send_keys(email)
                password_input.send_keys(password)
                sign_in_button.click()
            except:
                print("Failed to find login form. Continuing...")

            time.sleep(2)

            try:
                allow_button = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
                )
                allow_button.click()
            except:
                print("Failed to find 'Allow and Continue' button again. Continuing...")

            try:
                lecture_link = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[5]/div/div[5]/div[1]/div[3]/ul/li/a"))
                )
                lecture_link.click()
            except:
                print("Failed to find 'Lecture 12 poll questions' link. Continuing...")

            time.sleep(2)

            try:
                allow_button = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
                )
                allow_button.click()
            except:
                print("Failed to find 'Allow and Continue' button again. Continuing...")

            while True:
                try:
                    response_options = WebDriverWait(driver, 1).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.response.multiplechoice"))
                    )

                    num_options = len(response_options)

                    random_num = random.randint(0, num_options - 1)

                    response_options[random_num].click()
                except:
                    try:
                        input_field = WebDriverWait(driver, 1).until(
                            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[5]/div/div[5]/div[4]/form/input[2]"))
                        )

                        input_field.send_keys("ability to do stuff")
                        input("Press Enter to submit your response…")
                    except:
                        print("No question found. Waiting for 1 second and trying again…")
                        time.sleep(1)
                        continue

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = LearningCatalyticsUI()
    ui.run()
