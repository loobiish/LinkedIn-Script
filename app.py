# Importing Libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

# Setting path for edge driver
edge_path = Service("./webdriver/msedgedriver.exe")

# Setting Edge to start with maximized window
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('start-maximized')

# Creating an instance for the driver that we arfe going to use
driver = webdriver.Edge(service=edge_path, options=edge_options)

# Going to the LinkedIn Website
driver.get("https://linkedin.com")
time.sleep(10)
driver.quit()
