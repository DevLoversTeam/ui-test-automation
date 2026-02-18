from pages.main.components.footer import Footer


def test_main_footer(page, settings, steps):
    page.goto(settings.BASE_URL)
    steps.check("Open base URL", lambda: None)

    footer = Footer(page)

    steps.visible('Check "Built by DevLovers community." text', footer.built_by_text)
    steps.visible('Check "DevLovers" brand in footer', footer.devlovers_brand)
    steps.visible('Check "Privacy Policy" link', footer.privacy_policy)
    steps.visible('Check "Terms of Service" link', footer.terms_of_service)
    steps.visible('Check copyright text', footer.copyright_text)

    steps.visible('Check "System theme" button', footer.system_theme)
    steps.visible('Check "Light theme" button', footer.light_theme)
    steps.visible('Check "Dark theme" button', footer.dark_theme)

    steps.visible('Check "GitHub" link', footer.github_link)
    steps.visible('Check "LinkedIn" link', footer.linkedin_link)
    steps.visible('Check "Telegram" link', footer.telegram_link)