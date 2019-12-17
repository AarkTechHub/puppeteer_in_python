import asyncio
import json
from pyppeteer import launch
from time import sleep


async def main():
    browser = await launch({'headless':False,'autoClose':False})
    page = await browser.newPage()
    await page.goto('https://facebook.com')
    title = await page.title()
    print(title)

    ele = await page.waitForXPath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[3]/td[2]/div/a")
    print(ele)
    await ele.click()
    await page.waitForNavigation();
    await page.focus('#identify_email')
    await page.keyboard.type('9896438076')

    ele = await page.waitForXPath("/html/body/div[1]/div[3]/div[1]/div/div/div/form/div/div[3]/div/div[1]/label/input")
    await ele.click()
    await page.waitForNavigation()
    img = await page.waitForXPath("/html/body/div[1]/div[3]/div[1]/div/form/div/div[2]/table/tbody/tr/td[2]/div/div/div[1]/img")
    nameele = await page.waitForXPath("/html/body/div[1]/div[3]/div[1]/div/form/div/div[2]/table/tbody/tr/td[2]/div/div/div[2]/div")
    #print(img)
    imgsrc = await page.evaluate('(element) => element.src', img)
    name = await page.evaluate("(ele) => ele.textContent",nameele)
    print(imgsrc)
    print(name)
    sleep(20)
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())