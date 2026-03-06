from pages.main.components.header_auth import AuthHeader
from pages.main.login_page import LoginPage


def test_main_header_auth(page, settings, steps):
    steps.check("Login via **/login", lambda: LoginPage(page).login(settings.LOGIN, settings.PASSWORD))

    header = AuthHeader(page)

    # MainHeader fields
    steps.visible('Check "DevLovers" link', header.devlovers)
    steps.visible('Check "Q&A" link', header.qa)
    #steps.visible('Check "Quizzes" link', header.quizzes)
    steps.visible('Check "Leaderboard" link', header.leaderboard)
    steps.visible('Check "About" link', header.about)
    steps.visible('Check "Blog" link', header.blog)
    steps.visible('Check "Shop" link', header.shop)
    steps.visible('Check "GitHub Star" link', header.github_star)
    steps.visible('Check "Change language" button', header.change_language)

    # AuthHeader fields
    steps.visible('Check "Dashboard" link', header.dashboard)
    steps.visible('Check "Log out" button', header.logout)