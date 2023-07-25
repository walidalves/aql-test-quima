from behave import *
import time
from pages.aql_page import AqlPage
from pages.enviroment import TestEnvironment

# Chama o método before_all diretamente da classe TestEnvironment
TestEnvironment.before_all()

@given('we are on the AQL web site')
def step_impl_given(context):
    TestEnvironment.before_scenario(context)
    context.aql_page = AqlPage(context.test_environment.page)
    context.aql_page.open_website()
    context.aql_page.accept_cookies()
    context.aql_page.close_modal()


@when('we complete all fields of AQL Sampling Simulator')
def step_impl_when(context):
    time.sleep(5)
    context.aql_page.fill_quantity_with_random_number()


@then('behave show all value points')
def step_impl_then(context):
    context.aql_page.verify_value_points()
    context.aql_page.close_page()
    context.browser_instance.close()
    time.sleep(2)
