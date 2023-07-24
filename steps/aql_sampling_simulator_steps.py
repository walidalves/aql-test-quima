from behave import *
from playwright.sync_api import sync_playwright
import time

from pages.aql_page import AqlPage


@given('we are on the AQL web site')
def step_impl_given(context):
    with sync_playwright() as p:
        browser_instance = p.chromium.launch(headless=False)
        page = browser_instance.new_page()
        context.aql_page = AqlPage(page)
        context.aql_page.open_website()
        context.aql_page.accept_cookies()
        if context.aql_page.is_modal_visible():
            context.aql_page.close_modal()
        else:
            pass


@when('we complete all fields of AQL Sampling Simulator')
def step_impl_when(context):
    context.aql_page.fill_quantity_with_random_number()


@then('behave show all value points')
def step_impl_then(context):
    context.aql_page.verify_value_points()
    context.aql_page.close_page()
    time.sleep(2)
