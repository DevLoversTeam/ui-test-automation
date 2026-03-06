from pages.base_page import BasePage


class MainHeader(BasePage):

    @property
    def devlovers(self):
        return self.page.get_by_role("link", name="DevLovers")

    @property
    def qa(self):
        return self.page.get_by_role("link", name="Q&A")

    @property
    def quizzes(self):
        return self.page.get_by_role("link", name="Quizzes", exact=True)

    @property
    def leaderboard(self):
        return self.page.get_by_role("link", name="Leaderboard")

    @property
    def about(self):
        return self.page.get_by_role("link", name="About")

    @property
    def blog(self):
        return self.page.get_by_role("link", name="Blog")

    @property
    def shop(self):
        return self.page.get_by_role("link", name="Shop")

    @property
    def github_star(self):
        return self.page.get_by_role("link", name="Star on GitHub")

    @property
    def change_language(self):
        return self.page.get_by_role("button", name="Change language")