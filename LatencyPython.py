import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import calendar
import json
import requests

TIMEOUT = 60


def test_setup():
    global driver

    options = webdriver.ChromeOptions()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')

    # desired_capabilities = DesiredCapabilities.CHROME.copy()
    # desired_capabilities['acceptInsecureCerts'] = True

    # driver = webdriver.Remote(http://10.119.147.195:4444/wd/hub, desired_capabilities=desired_capabilities, options=webdriver.ChromeOptions())
    driver = webdriver.Remote(http://10.119.147.195:4444/wd/hub, options=options)
    webdriver.ChromeOptions()
    driver.maximize_window()



def test_home():
    driver.get(https://corona.its..net/CoronaUI/Login.htm?uid=abc@xyz.com&)
    driver.maximize_window()
    time.sleep(10)


def test_product():
               process_time = 0
    start_time = time.time()
    try:
        print("Do the Product Check")
        print(driver.title)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div/ul/li[8]/a").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/div[3]/div/div[1]/input").send_keys("R3B89A")
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[4]/div/a").click()
        time.sleep(10)
        process_time = time.time() - start_time
    except Exception as e:
        print("Time out on loading page! perhaps server is down?")
        program_management = 0
        raise e

    finally:
        # time.sleep(60)  # Wait so we can see what Edge is doing.
                              newrelicsend('Corona', 'Product', process_time)
        print("-product Check--took %s seconds ---" % process_time)
                              


def test_config():
               process_time = 0
    start_time = time.time()
    try:
        print("Do the Product Check")
        print(driver.title)
        driver.find_element(By.XPATH, "//a[contains(text(),'Config')]").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".generals:nth-child(2) > .ng-pristine").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input").send_keys("5133792103-01")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Get Data").click()
        time.sleep(10)

        process_time = time.time() - start_time1

    except Exception as e:
        print("Time out on loading page! perhaps server is down?")
        program_management = 0
        raise e

    finally:
        # time.sleep(60)  # Wait so we can see what Edge is doing.
                              newrelicsend('Corona', 'Config', process_time)
        print("-config Check--took %s seconds ---" % process_time)

def newrelicsend(system, operation, process_time):



    json_payload = "[{\"common\": {\"timestamp\":" + str(calendar.timegm(time.gmtime())) + ",\"attributes\":{\"appName\": \"215055 - SonarQube - Data ingest to NR\",\"system\": \""+system+"\",\"\
operation\": \""+operation+"\"}},\"metrics\":["
    json_payload += "{\"name\":\"process_time\",\"type\":\"gauge\", \"value\":" + str(process_time) + "}"
    json_payload += "]}]"



    proxies = {'https':''}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Api-Key': '348e84e3af0567f2934ed6f7a0715477FFFFNRAL'}
    data = json.loads(json_payload)
    req = requests.post('https://metric-api.newrelic.com//metric/v1', proxies=proxies, data=json_payload, headers=headers)
    # req = requests.post('https://metric-api.newrelic.com//metric/v1', data=json_payload, headers=headers)
    if req.status_code == 202:
        print("Metrics Added")
    else:
        print("Error while sending metrics to New Relic ("+str(req.status_code)+")")
        raise Exception("Error while sending metrics to New Relic ("+str(req.status_code)+")")
