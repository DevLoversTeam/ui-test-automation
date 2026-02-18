from pages.base_page import BasePage
from pages.main.components.header_unauth import UnauthHeader
from pages.main.login_page import LoginPage


def test_login(page, settings, steps):
    base = BasePage(page)

    steps.check("Open base URL", lambda: base.open(settings.BASE_URL).wait_ready())

    unauth_header = UnauthHeader(page)
    steps.check('Click "Log in" in unauth header', lambda: unauth_header.login.click())

    login_page = LoginPage(page)
    steps.visible('Verify "Log in" heading is visible', login_page.heading)

    steps.check("Fill email", lambda: login_page.email_input.fill(settings.LOGIN))
    steps.check("Fill password", lambda: login_page.password_input.fill(settings.PASSWORD))
    steps.check('Click "Log in" button', lambda: login_page.login_button.click())

    steps.check(
        'Validate URL is "https://www.devlovers.net/en/dashboard"',
        lambda: page.wait_for_url("https://www.devlovers.net/en/dashboard")
    )