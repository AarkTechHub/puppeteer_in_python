import asyncio
import json
from pyppeteer import launch


def loadDeviceDescriptors():
    devices = {}
    with open('DeviceDescriptor.json', 'r') as f:
        devicestore = json.load(f)

        # print(devicestore)
        for device in devicestore:
            devices[device['name']] = device

        return devices


async def main():
    devices = loadDeviceDescriptors()
    browser = await launch({'headless':False,'autoClose':False})
    page = await browser.newPage()

    await page.emulate(devices['iPhone X'])
    await page.goto('https://amazon.com')
    await page.focus("#nav-search-keywords")
    await page.keyboard.type('Raspberry Pi from Puppeteer')
    await page.screenshot({'path':"ScreenShots/keyboard.png"})
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())