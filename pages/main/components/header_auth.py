from pages.main.components.main_header import MainHeader


class AuthHeader(MainHeader):

    @property
    def user_menu(self):
        return self.page.get_by_role("button", name="User menu")
