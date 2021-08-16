import os

APPIUM_HOST = "http://localhost:4723/wd/hub"
SLEEP_BEFORE_INIT_UNITY_DRIVER = 20
PLATFORM = "android"

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

DESIRED_CAPABILITIES = {
    "platformName": "Some Platform",
    "appPackage": "App Bundle",
    "deviceName": "",
    "appActivity": "",
    "UDID": "",
    "noReset": True,
    "app": PATH("app/build.apk"),
}