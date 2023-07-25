from behave import *
from time import sleep
from playwright.sync_api import sync_playwright
from pages.aql_page import AqlPage


@given(u'we are on the AQL web site')
def step_impl(context):
    with sync_playwright() as p:
        context.browser = p.chromium.launch(headless=False)
        context.page = context.browser.new_page()
        context.aql_page = AqlPage(context.page)
        context.aql_page.open_website()
        context.aql_page.accept_cookies()
        context.aql_page.close_modal()
    sleep(5)

@when(u'we complete all fields of AQL Sampling Simulator')
def step_impl(context):
    context.aql_page.fill_quantity_with_random_number()
    context.page.wait_for_timeout(2000)
    sleep(5)

@then(u'behave show all value points')
def step_impl(context):
    sleep(5)
