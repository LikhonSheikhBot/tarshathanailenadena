from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
URL = 'https://charts.bogged.finance/0x3e07a8a8f260edeeca24139B6767A073918E8674'

def bogged():
    options = Options()
    options.headless = False
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
    driver.get(URL)
    time.sleep(2)

    try:
        supply = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/main/div/div/div/div[3]/div[1]/div/ul/li[3]/div"))
        )
        supply.click()

        c_supply = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/main/div/div/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/p/span[2]"))
        )
        c_supply = c_supply.text

        m_cap = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/main/div/div/div/div[1]/div[1]/div[2]/span[3]/h4"))
        )
        m_cap = m_cap.text
        volume = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/main/div/div/div/div[1]/div[1]/div[2]/span[1]/h4"))
        )
        volume = volume.text

        time.sleep(5)
    except:
        time.sleep(2)    
    finally:
        driver.quit()
        time.sleep(2)
        return c_supply, m_cap, volume

def bscscan():
    options = Options()
    options.headless = False
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
    driver.get('https://bscscan.com/token/0x3e07a8a8f260edeeca24139b6767a073918e8674')
    time.sleep(2)

    try:
        holders = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[4]/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/div"))
        )
        holders = holders.text
    except:
        time.sleep(2)    
    finally:
        driver.quit()
        return holders
  