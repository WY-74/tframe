from conftest import ENV

# For selenium
SELENIUM_CAPS = {"browserName": "chrome", "browserVersion": "99.0"}

# For Appium
APPIUM_CAPS = {
        "platfromName": "Android",
        "platfromVersion": "6.0.1",
        "noRest": "true",
        "dontStopAppOnReset": "true",
        "skipDeviceInitialization": "true",
        "unicodeKeyBoard": "true",
        }
APPIUM_ANDROID_CAPS = APPIUM_CAPS.update(
    {
        "appPackage": "com.tencent.wework",
        "appActivity": ".launch.LaunchSplashActivity",
        "deviceName": "qiyeweixin"
    }
)
APPIUM_IOS_CAPS = APPIUM_CAPS.update({})
