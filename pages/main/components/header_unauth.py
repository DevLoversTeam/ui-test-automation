from pages.main.components.main_header import MainHeader


class UnauthHeader(MainHeader):

    @property
    def login(self):
        return self.page.get_by_role("link", name="Log in")