import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'headless':False,'autoClose':False})
    # browser = await launch({'args':['--proxy-server=127.0.0.1:9009'],'headless':False,'autoClose':False}) ## for Proxy
    page = await browser.newPage()
    await page.setExtraHTTPHeaders({'Referer':'https://sparktoro.com/'})
    await page.goto('https://sparktoro.com/trending')
    await page.waitForSelector('div.title > a')

    stories = await page.evaluate('''() => {
        const links = Array.from(document.querySelectorAll('div.title > a'));
        return links.map(link => link.href).slice(0,10);
    }''')

    print(stories)
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())