import random
from playwright.sync_api import Page


class AqlPage:
    def __init__(self, page: Page):
        self.page = page

    def open_website(self):
        self.page.goto("https://www.qima.com/aql-acceptable-quality-limit")

    def fill_quantity_with_random_number(self):
        # Generate random number
        random_number = random.randrange(2, 214746)

        # Fill with the random number
        quantity_input = self.page.locator("input[name=\"aql-calculator-quantity\"]")
        quantity_input.fill(str(random_number))

    def accept_cookies(self):
        button_accept_cookies_selector = '#CybotCookiebotDialogBodyButtonAccept'
        button_accept_cookies = self.page.locator(button_accept_cookies_selector)
        button_accept_cookies.click()

    def is_modal_visible(self):
        modal_selector = 'button[title="Close (Esc)"].mfp-close'
        modal_element = self.page.locator(modal_selector)
        return modal_element.is_visible()

    def close_modal(self):
        #language modal
        button_close_modal = 'button[title="Close (Esc)"].mfp-close'

        if self.is_modal_visible():
            popup_element = self.page.locator(button_close_modal)
            popup_element.click()
