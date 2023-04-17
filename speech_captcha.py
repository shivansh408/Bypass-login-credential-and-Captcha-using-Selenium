from time import sleep
import requests
from PIL import Image
import pytesseract
from pytesseract import image_to_string
from selenium import webdriver

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract'

profile = webdriver.FirefoxProfile()

browser = webdriver.Firefox(profile)
browser.get('https://services.gst.gov.in/services/login')
browser.implicitly_wait(5)

username_inp = browser.find_element_by_css_selector("input[name='user_name']")
password_inp = browser.find_element_by_css_selector("input[id='user_pass']")

username_inp.send_keys("username")
password_inp.send_keys("password")

source = browser.find_element_by_xpath('//img[starts-with(@id, "imgCaptcha")]')
src = source.get_attribute("src")
print(src)
browser.get(src)

browser.save_screenshot('captcha.png')
base_image = Image.open('captcha.png')
base_image.save('captcha.png')

# Using pytesseract to read the text in the reCAPTCHA image
captcha_text = image_to_string(Image.open('captcha.png'))
print(captcha_text)

browser.get('https://services.gst.gov.in/services/login')

username_input = browser.find_element_by_css_selector("input[name='user_name']")
username_input.send_keys("username")

password_input = browser.find_element_by_css_selector("input[id='user_pass']")
password_input.send_keys("password")

captcha_input = browser.find_element_by_css_selector("input[name='captcha']")
captcha_input.send_keys(captcha_text)

# This will Enter the captcha text in the form

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(5)

browser.close()