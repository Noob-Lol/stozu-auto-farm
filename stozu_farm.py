from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
script_path = os.path.abspath(os.path.dirname(__file__))
options=webdriver.ChromeOptions()
#options.binary_location = (f'{script_path+'/App/Chrome-bin/chrome.exe'}')
options.add_argument(f'user-data-dir={script_path+'/Data/profile'}')
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

#code starts here
driver.get(f'file://{script_path+"/test.html"}')
time.sleep(10)
driver.switch_to.window(driver.window_handles[1])

#after passing clouflare check and logging in
input("Press Enter to start farm...")
print('Script started, press Ctrl+C to exit')
driver.minimize_window()
while True:
    driver.get('https://dash.stozu.net/earn/lv')
    WebDriverWait(driver, 15,0.2).until(EC.url_to_be('https://dash.stozu.net/earn'))
