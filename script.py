from fastapi import FastAPI
import asyncio
from playwright.async_api import async_playwright, Playwright
import logging
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format=(
        "%(asctime)s | %(levelname)-6s | logger=%(name)s | %(filename)s[%(funcName)s()]:L%(lineno)-4d |  %(message)s"
    ),
    level=logging.INFO,
)

app = FastAPI()

async def run(playwright: Playwright):
    proxy_server = os.getenv('PROXY_SERVER')
    proxy_username = os.getenv('PROXY_USERNAME')
    proxy_password = os.getenv('PROXY_PASSWORD')

    chromium = playwright.chromium
    browser = await chromium.launch(proxy={
        'server': proxy_server,
        'username': proxy_username,
        'password': proxy_password,
    })
    context = await browser.new_context(ignore_https_errors=True)
    page = await context.new_page()
    await page.set_extra_http_headers({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    })
    await page.goto(url="https://www.instagram.com/google/?hl=en")
    await page.wait_for_timeout(5000)
    html_content = await page.content()
    return(html_content)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/scrape")
async def scrape():
    async with async_playwright() as playwright:
        return await run(playwright)