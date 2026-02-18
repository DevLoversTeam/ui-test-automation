from pages.main.components.header_unauth import UnauthHeader


def test_main_header_unauth(page, settings, steps):
    page.goto(settings.BASE_URL)
    steps.check("Open base URL", lambda: None)

    header = UnauthHeader(page)
    # MainHeader fields
    steps.visible('Check "DevLovers" link', header.devlovers)
    steps.visible('Check "Q&A" link', header.qa)
    steps.visible('Check "Quizzes" link', header.quizzes)
    steps.visible('Check "Leaderboard" link', header.leaderboard)
    steps.visible('Check "About" link', header.about)
    steps.visible('Check "Blog" link', header.blog)
    steps.visible('Check "Shop" link', header.shop)
    steps.visible('Check "GitHub Star" link', header.github_star)
    steps.visible('Check "Change language" button', header.change_language)

    # UnauthHeader fields
    steps.visible('Check "Log in" link', header.login)