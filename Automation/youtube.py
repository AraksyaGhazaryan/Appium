from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.google.com")








