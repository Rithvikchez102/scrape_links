# from main import page

def next_button(page):

    next_button = page.get_by_text("Next", exact=True).click()

    return next_button