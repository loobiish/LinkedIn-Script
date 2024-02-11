# Importing Libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting path for edge driver
edge_path = Service("./webdriver/msedgedriver.exe")

# Setting Edge to start with maximized window
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('start-maximized')

# Creating an instance for the driver that we arfe going to use
driver = webdriver.Edge(service=edge_path, options=edge_options)

# Going to the LinkedIn Website
def open_linkedin():
    try:
        driver.get("https://linkedin.com")
        time.sleep(5)
    except Exception as e:
        print(f"Failed to open LinkedIn due to following error: {e}")

# Dealing with Login Page
def login_to_account(email, password):
    try:
        # Filling Login Information
        # Enter Email
        login_email = driver.find_element("id", "session_key")
        login_email.send_keys(email)

        # Enter Password
        login_password = driver.find_element("id", "session_password")
        login_password.send_keys(password)

        # Clicking on Sign In Button
        # Waiting for 5 seconds so that we can successfully give input to the  fields before clicking on it
        """ 
        Basic difference between the below method to get an element and the above method is we can wait for 
        some specific amount of time in the below method. It is useful when our targeted element takes some time 
        to load or we are waiting for some tasks to complete.
        """
        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')))
        login_button.click()
        
    except Exception as e:
        print(f"Failed to login due to following error: {e}")

# Dealing with the Feed Page
def linkedIn_feed_page(companyName):
    # Our main aim is to search for a specific company and open it's page
    # ```````Right now we are trying to search a person`
    try:
        search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        search_bar.send_keys(companyName)
        search_bar.send_keys(Keys.ENTER)

    except Exception as e:
        print(f"Failed to reach Profile Page due to following error: {e}")

# Dealing with the Search Page and checking the company we have searched
def check_company():
    try:
        open_company_page = driver.find_element(By.CSS_SELECTOR, '#XXDyYpf3SwCCY34w2QHaPg\=\= > div > ul > li > div > a > div > div.search-nec__hero-kcard-v2-actions > div:nth-child(2) > div > a')
        print("#####################################################")
        print(open_company_page)
        print("*******************************************************")
        # open_company_page = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="XXDyYpf3SwCCY34w2QHaPg=="]/div/ul/li/div/a/div/div[2]/div[2]')))
        open_company_page.click()
        
    except Exception as e:
        print(f"Failed to open the page of company due to following error: {e}")


open_linkedin()
login_to_account(email="loobiish@gmail.com", password="lavishK@01")
linkedIn_feed_page(companyName="Google")
check_company()
time.sleep(10)
driver.quit()
