from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@step('I open the url "{url}"')
def step_open_url(context, url):
    context.behave_driver.get(url)

@when('I input "{text}" into the search field with id "{field_id}"')
def step_input_text(context, text, field_id):
    search_field = context.behave_driver.find_element(By.ID, field_id)
    search_field.clear()
    search_field.send_keys(text)

@when('I click the element with type "{element_type}"')
def step_click_element_type(context, element_type):
    wait = WebDriverWait(context.behave_driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".clcbtn")))
    context.behave_driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()

@then('I expect that the element with class "{element_id}" contains the text "{text}"')
def step_verify_text_by_id(context, element_id, text):
    element = context.behave_driver.find_element(By.CSS_SELECTOR, ".oOutp")
    element_text = element.text.strip()
    assert text in element_text, f"Expected '{text}' to be in '{element_text}'"