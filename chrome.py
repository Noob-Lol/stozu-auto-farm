#Opens chrome with custom profile
import os
import subprocess
script_path = os.path.abspath(os.path.dirname(__file__))
chrome_path = os.path.expandvars('%LOCALAPPDATA%/Chromium/Application/chrome.exe')
if chrome_path:
    subprocess.run([chrome_path, (f'--user-data-dir={script_path+'/User Data'}')])
else: print('Ungoogled Chromium not found. Install it.')