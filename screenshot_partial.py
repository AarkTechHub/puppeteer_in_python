import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'headless':False,'autoClose':False})
    page = await browser.newPage()
    screenshotoptions = {'path': 'ScreenShots/test_partial.png', 'fullPage': False,
                         'clip': {'x': 0, 'y': 0, 'width': 1280, 'height': 150}}
    await page.setViewport({'width': 1280, 'height': 800})
    await page.goto("https://amazon.com",{'timeout':120000})

    await page.screenshot(screenshotoptions)
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
