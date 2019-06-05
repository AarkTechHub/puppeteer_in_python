import asyncio
import json
from pyppeteer import launch


def loadDeviceDescriptors():
    devices = {}
    with open('DeviceDescriptor.json', 'r') as f:
        devicestore = json.load(f)

        # print(devicestore)
        for device in devicestore:
            print(device)
            devices[device['name']] = device

        return devices


async def main():
    devices = loadDeviceDescriptors()
    browser = await launch({'headless': False,'autoClose':False})
    page = await browser.newPage()
    await page.emulate(devices['iPhone X'])
    await page.goto('https://amazon.com')
    await page.screenshot({'path': 'Imgs/test-device_emulation.png'})
    await browser.close()



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())