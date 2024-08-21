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
    try:
        time.sleep(5)
        search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        search_bar.send_keys(companyName)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)

    except Exception as e:
        print(f"Failed to reach Profile Page due to following error: {e}")

# Dealing with the Search Page and checking the company we have searched
def check_company():
    # We will click on View Company button to open the company's LinkedIn Page
    try:
        time.sleep(5)
        open_company_page = driver.find_element(By.CLASS_NAME, 'app-aware-link.full-width.artdeco-button.artdeco-button--default.artdeco-button--2.artdeco-button--muted.artdeco-button--secondary')
        open_company_page.click()
        
    except Exception as e:
        print(f"Failed to open the page of company due to following error: {e}")

# Search for a particular person or keyword in Company's profile
def search_in_profile(keyword, message):
    try:
        # First we need to click on People button
        people_btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[3]/nav/ul/li[5]/a')))
        time.sleep(3)
        people_btn.click()

        # Now we need to search for the keyword in the search bar
        time.sleep(5)
        search_keyword = driver.find_element(By.ID, "people-search-keywords")
        search_keyword.send_keys(keyword)
        search_keyword.send_keys(Keys.ENTER)
        time.sleep(5)
        
        # Now our task is to click on connect and send a note to the particular user that we have found
        connect_person = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/div/div[1]/ul/li/div/section/footer/button')))
        connect_person.click()
        
        # Click the add note button
        add_note_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')))
        add_note_button.click()
        
        # Now we want to send the connection request with a short message 
        connection_message = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/div[1]/textarea')))
        connection_message.send_keys(message)
        time.sleep(5)
        
        # Click on send button
        send_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[4]/button[2]')))
        send_button.click()
    
    except Exception as e:
        print(f"Failed to find 'People' Button or Search particular keyword due to following error: {e}")


# Calling Funtions
open_linkedin()
login_to_account(email="mehtanitin2000@gmail.com", password="mehta1762000")

# For human verification
time.sleep(40) 

linkedIn_feed_page(companyName="Amaha (formerly InnerHour)")
check_company()
search_in_profile(keyword="Senior Product Designer", message="Hi, It's good to connect to you !")
time.sleep(15)
driver.quit()
