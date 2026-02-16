from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
	driver = webdriver.Chrome()
	driver.get("http://127.0.0.1:5500/index.html")

	driver.find_element(By.ID, "username").send_keys("testuser")
	driver.find_element(By.ID, "password").send_keys("testpassword")
	driver.find_element(By.ID, "login-button").click()

	message = driver.find_element(By.ID, "login-success").text
	assert "Login successful!" in message

	driver.quit()