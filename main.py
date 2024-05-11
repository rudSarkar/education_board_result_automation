import re
import os
from time import sleep
from dotenv import load_dotenv, dotenv_values
from playwright.sync_api import Playwright, sync_playwright, expect

pdf_saved = False
load_dotenv()

def run(playwright: Playwright) -> None:
    global pdf_saved
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.educationboardresults.gov.bd/")
    page.locator("#exam").select_option(f"{os.getenv('exam_name')}")
    page.locator("#year").select_option(f"{os.getenv('exam_year')}")
    page.locator("#board").select_option(f"{os.getenv('exam_board')}")
    page.locator("#roll").click()
    page.locator("#roll").fill(f"{os.getenv('exam_roll')}")
    page.locator("#roll").press("Tab")
    page.locator("#reg").fill(f"{os.getenv('exam_reg')}")
    
    text = page.locator(
        "body > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > form > table > tbody > tr > td:nth-child(2) > fieldset > table > tbody > tr:nth-child(7) > td:nth-child(2)"
    ).inner_text()

    numbers = [int(num) for num in text.split('+')]
    value_sum = sum(numbers)

    page.locator("#value_s").click()
    page.locator("#value_s").fill(f"{value_sum}")

    page.get_by_role("button", name="Submit").click()

    sleep(4)
    try:
        get_search_again = page.locator(
            "body > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(3) > td > a"
        ).wait_for(timeout=3000).inner_text()

        if get_search_again == "Search Again":
            page.pdf(path='result.pdf')
            pdf_saved = True
    except:
        pdf_saved = False

    check_file = os.path.isfile("./result.pdf")
    if check_file:
        pdf_saved = True

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    while not pdf_saved:
        run(playwright)
        