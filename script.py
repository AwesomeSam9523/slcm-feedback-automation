from selenium import webdriver
import platform
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

system_platform = platform.system()
load_dotenv()

USERNAME = os.getenv("FIRST_NAME") + "." + os.getenv("REGISTRATION_NUMBER")
PASSWORD = os.getenv("PASSWORD")

if not USERNAME or not PASSWORD:
	raise ValueError("Please provide the required environment variables.\n"
					 "Check README.md on GitHub: https://github.com/AwesomeSam9523/slcm-feedback-automator")


chrome_options = Options()
if system_platform == "Windows":
	chrome_options.add_experimental_option("detach", True)
if system_platform == "Darwin":
	chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

browser = webdriver.Chrome(options=chrome_options)
a = [browser]

def login(login_page ="https://mujslcm.jaipur.manipal.edu/Home/Index"):
	browser.get(login_page)
	browser.implicitly_wait(5)

	username_field = browser.find_element("name", "UserName")
	password_field = browser.find_element("name", "Password")
	username_field.send_keys(USERNAME)
	password_field.send_keys(PASSWORD)
	browser.implicitly_wait(3)
	login_button = browser.find_element("id", "login_submitStudent")
	login_button.click()
	print('Logged in!')


def list_all_feedbacks(feedback_page="https://mujslcm.jaipur.manipal.edu/Student/Survey/FeedbackList"):
	browser.get(feedback_page)
	feedbacks_fetch = browser.find_elements("class name", "btn-clean")

	return [{"status": feedback.text, "link": feedback.get_attribute('href')} for feedback in feedbacks_fetch]

def fill_feedback(course_link):
	browser.get(course_link)

	no_buttons = browser.find_elements("xpath", "//input[@type='radio' and @class='yescheck']")
	for button in no_buttons:
		button.click()
	
	from selenium.webdriver.support.ui import Select
	dropdowns = browser.find_elements("xpath", "//select")
	for dropdown in dropdowns:
		select = Select(dropdown)
		select.select_by_value("Y")
	
	text_box = browser.find_element("xpath", "//textarea")
	text_box.send_keys("Great Experience.")
	
	submit_button = browser.find_element("xpath", "//button[@id='btnSubmit']")
	submit_button.click()

	browser.get("https://mujslcm.jaipur.manipal.edu/Student/Survey/FeedbackList")

login()
feedbacks = list_all_feedbacks()
print(feedbacks)
for feedback in feedbacks:
	print(a)
	if feedback["status"] == "Pending":
		fill_feedback(feedback["link"])
		feedback["status"] = "Completed"
	else:
		continue
