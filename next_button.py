# from main import page

def next_button(page):

    # next_button = page.get_by_text("Next", exact=True).click()
    page.get_by_role("button", name="Load more").click()
    page.wait_for_timeout(2000)
    # return next_button