from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser


def get_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Visit the page
        page.goto(url)
        page.wait_for_selector('table', timeout=40000)  
        page.wait_for_load_state('networkidle') 
        page.wait_for_timeout(5000)  


        html_body = page.inner_html('body')
        browser.close()

        parse_html = HTMLParser(html_body)
        return parse_html