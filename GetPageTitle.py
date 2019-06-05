import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'headless': False, 'autoClose': False})
    page = await browser.newPage()

    await page.goto('https://google.com')
    title = await page.title()
    print(title)
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())