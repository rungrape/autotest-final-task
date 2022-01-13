#4.3, task 6
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.custom_page_with_ny_promo import CustomNewYearPromoPage


def test_guest_can_add_product_to_basket(get_browser_driver):
	driver = get_browser_driver
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = CustomNewYearPromoPage(link, driver)
	page.open()
	page.should_be_discount()

def test_guest_cant_see_success_message_after_adding_product_to_basket(get_browser_driver):
	driver = get_browser_driver
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
	page = CustomNewYearPromoPage(link, driver)
	page.open()
	page.is_not_element_present(ADD_TO_BASKET_BTN)

def test_guest_cant_see_success_message(get_browser_driver):

def test_message_disappeared_after_adding_product_to_basket(get_browser_driver):


