from playwright.sync_api import sync_playwright

class TestEnvironment:
    # Defina before_all como método estático (staticmethod)
    @staticmethod
    def before_all():
        with sync_playwright() as playwright:
            TestEnvironment.browser = playwright.chromium.launch(headless=False)
            TestEnvironment.page = TestEnvironment.browser.new_page()
            TestEnvironment.page.goto("https://www.qima.com/aql-acceptable-quality-limit")
            TestEnvironment.page.get_by_role("button", name="Permitir todos").click()

    @staticmethod
    def before_scenario(context):
        # Compartilha o ambiente de teste com o contexto do cenário
        context.test_environment = TestEnvironment

    @staticmethod
    def after_all():
        # Fecha o navegador após a execução de todos os cenários
        TestEnvironment.page.close()
        TestEnvironment.browser.close()

