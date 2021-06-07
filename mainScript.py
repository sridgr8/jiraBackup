from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()

preferences = {"download.default_directory": "C:\SrinivasCode\jiraBackup\Downloads", "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs",preferences)

driver = webdriver.Chrome(executable_path="./webDrivers/chromedriver.exe", chrome_options=options)

driver.maximize_window()

# Open Jira Website

driver.get("https://onprem.atlassian.net/secure/Dashboard.jspa?lastVisited=true")

# Log into Jira

driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[1]/div/header/div/a/div/button").click() #Click Signin button

# Enter Email
txtEmail=driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[1]/div/div/div/div/div/input")
txtEmail.send_keys("srinivasulu.kummitha@qualitestgroup.com")
txtEmail.send_keys(Keys.RETURN)

# Enter Password
driver.implicitly_wait(10)
txtPassword=driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[2]/div/div/div/div/div/div/div/input")
txtPassword.send_keys("pwd here")



# Click Enter to Signin
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[3]/button").click()
driver.implicitly_wait(10)

# Start Loop

# Open Jira Ticket URL
driver.get("https://onprem.atlassian.net/browse/PVHDAM-1483")

# Download Attachments
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[5]/div[5]/div/div[1]/div/div[1]/div/div/div[1]/div/div/button").click() #Click the 3 dots next to Attachments

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[5]/div[5]/div/div[1]/div/div[1]/div/div/div[3]/div/div/div/div/div/span[2]/span[1]/span").click() #Click the Download All Link


# Open JIRA Print Page

# Print Jira to PDF

# End Loop

# Close ChromeDriver
# driver.close()

