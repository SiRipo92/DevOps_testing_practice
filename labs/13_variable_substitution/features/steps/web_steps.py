# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Web Steps
Steps file for web interactions with Selenium
For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""

from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I am on the "Home Page"')
def step_impl(context):
    context.response = context.driver.get(context.base_url)

@when('I set the "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = "pet_" + element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_string)

@when('I click the "{button}" button')
def step_impl(context, button):
    button_id = button.lower() + '-btn'
    element = context.driver.find_element(By.ID, button_id)
    element.click()

@then('I should see the message "{message}"')
def step_impl(context, message):
    element = context.driver.find_element(By.ID, 'flash_message')
    assert message in element.text

@then('I should see "{search_text}" in the results')
def step_impl(context, search_text):
    element = context.driver.find_element(By.ID, 'search_results')
    assert search_text in element.text

@then('I should not see "{search_text}" in the results')
def step_impl(context, search_text):
    element = context.driver.find_element(By.ID, 'search_results')
    assert search_text not in element.text

