import time
import json
import os
import shutil
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Variables
username="srinivasulu.kummitha@qualitestgroup.com"
password=""
downloadPath="D:\Onprem Jira Backup\\"
csv_file_name='data2.csv'

options=webdriver.ChromeOptions()

settings = {
    "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }

preferences = {'printing.print_preview_sticky_settings.appState': json.dumps(settings), "download.default_directory": downloadPath, "savefile.default_directory": downloadPath, "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs",preferences)
options.add_argument('--kiosk-printing')

driver = webdriver.Chrome(executable_path="./webDrivers/chromedriver.exe", chrome_options=options)

driver.maximize_window()

def login_to_jira():
    # Open Jira Website
    driver.get("https://onprem.atlassian.net/secure/Dashboard.jspa?lastVisited=true")

    # Log into Jira
    driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[1]/div/header/div/a/div/button").click() #Click Signin button

    # Enter Email
    txtEmail=driver.find_element(By.XPATH, "//*[@id=\"username\"]")
    txtEmail.send_keys(username)
    txtEmail.send_keys(Keys.RETURN)

    # Enter Password
    driver.implicitly_wait(10)
    txtPassword=driver.find_element(By.XPATH, "//*[@id=\"password\"]")
    txtPassword.send_keys(password)

    # Click Enter to Signin
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[3]/button").click()

def download_attachments(ticket_id):
    # Open New Tab
    time.sleep(10)
    ticketURL="https://onprem.atlassian.net/secure/issueAttachments/"+ticket_id+".zip"
    driver.execute_script('''window.open("'''+ticketURL+'''", "_blank");''')
    time.sleep(15)

def open_new_tab_pdf(ticketNumber):
    # Open New Tab
    time.sleep(3)
    ticketURL="https://onprem.atlassian.net/si/jira.issueviews:issue-html/"+ticketNumber+"/"+ticketNumber+".html"
    driver.execute_script('''window.open("'''+ticketURL+'''", "_blank");''')
    time.sleep(5)

def download_pdf():
    # Open JIRA Print Page
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(3)
    # Print Jira to PDF
    driver.execute_script('window.print();')

def close_new_tab():
    # Close current tab
    driver.switch_to_window(driver.window_handles[1])
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

def close_driver():
    # Close ChromeDriver
    print("Closing ChromeDriver")
    driver.quit()

def move_files(ticketNumber):
    source = downloadPath
    os.mkdir(downloadPath + ticketNumber)
    dest = downloadPath + ticketNumber

    files = os.listdir(source)

    for f in files:
        if (f.startswith("[#"+ticketNumber)):
            shutil.move(source+f, dest)
        if (f.startswith(ticketNumber+".zip")):
            shutil.move(source+f, dest)

# Function Calls-----------------------------------------------------------------------------------------------------------------

login_to_jira()

# Start Loop
print("Execution Started")

with open(csv_file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        ticketNumber=row[0]
        ticket_id=row[1]
        
        # Download attachments of the ticket
        download_attachments(str(ticket_id))
        # download_attachments()
        # close_new_tab()

        # Download PDF file of the ticket
        open_new_tab_pdf(str(ticketNumber))
        download_pdf()
        close_new_tab()

        # Move Files to appropriate folder
        move_files(str(ticketNumber))

        print("Downloaded Data of "+ticketNumber)

close_driver()

print("Execution Completed")

# Function Calls-----------------------------------------------------------------------------------------------------------------
