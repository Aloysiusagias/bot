from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

device = devices[0]

device.shell("input swipe 353 510 353 510 1000")
device.shell("input swipe 500 1400 500 800 300")
device.shell("input tap 72 140")