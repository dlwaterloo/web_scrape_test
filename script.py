from fastapi import FastAPI
import asyncio
from playwright.async_api import async_playwright, Playwright
import logging

logging.basicConfig(
    format=(
        "%(asctime)s | %(levelname)-6s | logger=%(name)s | %(filename)s[%(funcName)s()]:L%(lineno)-4d |  %(message)s"
    ),
    level=logging.INFO,
)

app = FastAPI()

async def run(playwright: Playwright):
    chromium = playwright.chromium
    chromium_path = chromium.executable_path  # This is the new line to add
    print(f"Chromium Path: {chromium_path}")  # This will log the Chromium path
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.set_extra_http_headers({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
  })
    await page.goto(url="https://www.instagram.com/social__ai/?hl=en")
    await page.wait_for_timeout(3000)
    html_content = await page.content()
    print(html_content)
    # other actions...
    await browser.close()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/scrape")
async def scrape():
    async with async_playwright() as playwright:
        return await run(playwright)