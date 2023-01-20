from utils.chrome_browser import SingletonChromeBrowser


def before_all(context):
    context.browser = SingletonChromeBrowser()


def after_scenario(context, scenario):
    context.browser.clear()


def after_all(context):
    context.browser.quit()
