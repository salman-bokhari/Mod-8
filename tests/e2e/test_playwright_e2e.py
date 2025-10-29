import time
from playwright.sync_api import sync_playwright

def test_e2e_calculation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://127.0.0.1:8000/')
        page.fill('#a','7')
        page.fill('#b','8')
        page.select_option('#op','add')
        page.click('#go')
        # wait for result text to appear
        page.wait_for_selector('#result')
        text = page.inner_text('#result')
        assert 'Result: 15' in text
        browser.close()
