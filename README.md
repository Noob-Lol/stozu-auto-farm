# this code is outdated and patched
**New version is at https://github.com/Noob-Lol/stozu-auto-farm-v2**
## What is this:
Automated credit farm on [stozu](https://dash.stozu.net/), speed is ~45 per minute, depends on your device perfomance and browser settings.

Made on Python with Selenium WebDriver. Custom chrome profile included.
# Requirements:
- [Python](https://www.python.org/downloads/), selenium: ```pip install selenium```
- [Ungoogled Chromium](https://github.com/ungoogled-software/ungoogled-chromium-windows/releases/latest), download and run installer
# How to use:
If you want to change or check the browser settings: ```py chrome.py```
- Run script: ```py stozu_farm.py```
## Optional:
Add this to ublock filters (it will hide all content and increase speed):
```
dash.stozu.net##.wrapper
linkvertise.com##lv-root
```
## Ask questions:
In github issues, n01b on discord, https://discord.gg/NoobNetwork
