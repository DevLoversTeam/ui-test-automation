from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://www.devlovers.net/en/login"

    @property
    def heading(self):
        return self.page.get_by_role("heading", name="Log in")

    @property
    def continue_google(self):
        return self.page.get_by_role("button", name="Continue with Google")

    @property
    def continue_github(self):
        return self.page.get_by_role("button", name="Continue with GitHub")

    @property
    def email_input(self):
        return self.page.get_by_role("textbox", name="Email")

    @property
    def password_input(self):
        return self.page.get_by_role("textbox", name="Password")

    @property
    def show_password(self):
        return self.page.get_by_role("button", name="Show password")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Log in")

    @property
    def signup_link(self):
        return self.page.get_by_role("link", name="Sign up")

    def open(self):
        super().open(self.URL).wait_ready()
        return self

    def login(self, email: str, password: str):
        self.open()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_url("**/dashboard")
        return self