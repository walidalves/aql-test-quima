import random
from playwright.sync_api import Page


class AqlPage:
    def __init__(self, page: Page):
        self.page = page

    def open_website(self):
        self.page.goto("https://www.qima.com/aql-acceptable-quality-limit")

    def get_quantity_input(self):
        # get input field
        quantity_input = self.page.locator('input[name="aql-calculator-quantity"]')
        return quantity_input

    def fill_quantity_with_random_number(self):
        # Generate random number
        random_number = random.randint(2, 214748366)

        # Fill with the random number
        quantity_input = self.get_quantity_input()
        quantity_input.fill(str(random_number))

    def accept_cookies(self):
       button_accept_cookies_selector = '#CybotCookiebotDialogBodyButtonAccept'
       button_accept_cookies = self.page.locator(button_accept_cookies_selector)
       button_accept_cookies.click()


    def is_modal_visible(self):
        # Defina o seletor para o modal que deseja verificar a visibilidade
        modal_selector = 'button[title="Close (Esc)"].mfp-close'
        modal_element = self.page.locator(modal_selector)
        return modal_element.is_visible()

    def close_modal(self):
       #lenguage modal
        button_first_popup = 'button[title="Close (Esc)"].mfp-close'
        popup_element = self.page.locator(button_first_popup)
        popup_element.click()