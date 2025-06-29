# from main import page

def next_button(page):

    # next_button = page.get_by_text("Next", exact=True).click()
    # page.get_by_role("button", name="Load more").click()
    # page.get_by_test_id("page-next").click()
    # next_button = page.get_by_role("button", name="Go to next page").click()
    # next_button = page.locator("a").filter(has_text="Next Events").click()
    # next_button = page.get_by_role("link", name="Next page").nth(1).click()
    # next_button = page.get_by_role("link", name="Load more opportunities").click()
    # next_button = page.locator("#point_iframe").content_frame.get_by_test_id("link-next-button-pagination").click()
    # next_button =  page.get_by_role("link", name="Load more opportunities").click()
    # next_button =   page.get_by_role("link", name="Next Page").nth(1).click()
    # next_button = page.get_by_role("link", name="→").click()



    page.wait_for_timeout(60000)
    # return next_button