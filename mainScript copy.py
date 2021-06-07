from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()

preferences = {"download.default_directory": "C:\SrinivasCode\jiraBackup\Downloads", "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs",preferences)

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.whatsapp.com/download/?lang=en")

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/div[2]/a").click()

