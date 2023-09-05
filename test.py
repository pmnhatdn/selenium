from seleniumwire import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

service = EdgeService(executable_path=EdgeChromiumDriverManager().install())

driver = webdriver.Edge(service=service)
driver.get('https://scrapeme.live/shop/')
body = driver.find_element(By.TAG_NAME, 'body')
print(body.text)
print(driver.requests)

# Kill browser instance
driver.quit()
