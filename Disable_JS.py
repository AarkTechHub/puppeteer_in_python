import asyncio
from pyppeteer import launch

async def interceptRequest(request):

    if request.resourceType == 'script':

        await request.abort()
    else:
        await request.continue_()

async def main():
    browser = await launch({'headless': False, 'autoClose': False})
    page = await browser.newPage()
    await page.setRequestInterception(True)
    page.on('request',
            lambda request: asyncio.ensure_future(interceptRequest(request)))

    await page.goto('https://www.youtube.com')
    title = await page.title()
    print(title)
    await page.screenshot({'path': 'ScreenShots/test-device_disable_js.png'})
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())