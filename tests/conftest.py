import pytest
from playwright.sync_api import sync_playwright, expect
from config import settings as app_settings


@pytest.fixture(scope="session")
def settings():
    return app_settings


@pytest.fixture(scope="session")
def browser(settings):
    with sync_playwright() as p:
        browser_type = getattr(p, settings.BROWSER)
        browser = browser_type.launch(headless=settings.HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, settings):
    context = browser.new_context(base_url=settings.BASE_URL or None)
    page = context.new_page()
    page.set_default_timeout(settings.TIMEOUT)
    yield page
    context.close()


@pytest.fixture
def steps(request):
    request.node.test_steps = []

    class Steps:
        @staticmethod
        def log(message: str):
            request.node.test_steps.append(message)
            print(message)

        def check(self, description: str, fn):
            try:
                fn()
            except Exception as e:
                self.log(f'FAIL: {description} -> {type(e).__name__}: {e}')
                raise
            else:
                self.log(f'PASS: {description}')

        def visible(self, description: str, locator):
            self.check(description, lambda: expect(locator).to_be_visible())

    return Steps()