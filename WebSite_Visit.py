import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()

    await page.setViewport({'width': 1280, 'height': 800})
    await page.goto('https://rush49.com')
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())