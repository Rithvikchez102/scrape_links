import re
from playwright.sync_api import Playwright, sync_playwright, expect




def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    output_file = input("Enter the output file name: ")

    from scrapping import scrape

    links = scrape(page)

    with open(output_file, "w") as f:
        for link in links:
            f.write(link + "\n")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:


    run(playwright)
