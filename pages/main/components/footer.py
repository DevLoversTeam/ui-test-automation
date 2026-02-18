from datetime import datetime

from pages.base_page import BasePage


class Footer(BasePage):

    @property
    def built_by_text(self):
        return self.page.get_by_text("Built by DevLovers community.")

    @property
    def devlovers_brand(self):
        return self.page.locator("footer").get_by_text("DevLovers", exact=True)

    @property
    def privacy_policy(self):
        return self.page.get_by_role("link", name="Privacy Policy")

    @property
    def terms_of_service(self):
        return self.page.get_by_role("link", name="Terms of Service")

    @property
    def copyright_text(self):
        return self.page.get_by_text(f"© {datetime.now().year} DevLovers")

    @property
    def system_theme(self):
        return self.page.get_by_role("button", name="System theme")

    @property
    def light_theme(self):
        return self.page.get_by_role("button", name="Light theme")

    @property
    def dark_theme(self):
        return self.page.get_by_role("button", name="Dark theme")

    @property
    def github_link(self):
        return self.page.get_by_role("link", name="GitHub", exact=True)

    @property
    def linkedin_link(self):
        return self.page.get_by_role("link", name="LinkedIn")

    @property
    def telegram_link(self):
        return self.page.get_by_role("link", name="Telegram")