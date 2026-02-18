from pages.main.components.main_header import MainHeader


class AuthHeader(MainHeader):

    @property
    def dashboard(self):
        return self.page.get_by_role("link", name="Dashboard")

    @property
    def logout(self):
        return self.page.get_by_role("button", name="Log out")