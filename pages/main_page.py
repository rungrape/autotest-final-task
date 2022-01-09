from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
	"""main page basic class"""
	def should_be_login_link(self):
		assert self.is_element_present(MainPageLocators.LOGIN_LINK), "Login link is not presented"

	def go_to_login_page(self):
		login_link = self.driver.find_element(By.CSS_SELECTOR, MainPageLocators.LOGIN_LINK)
		login_link.click()
