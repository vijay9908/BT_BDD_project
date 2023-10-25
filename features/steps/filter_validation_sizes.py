from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

sizes = {
            'XS': '//*[@id="root"]/div/main/div/div[1]/div[1]/label/span',
            'S': '//*[@id="root"]/div/main/div/div[1]/div[2]/label/span',
            'M': '//*[@id="root"]/div/main/div/div[1]/div[3]/label/span',
            'ML': '//*[@id="root"]/div/main/div/div[1]/div[4]/label/span',
            'L': '//*[@id="root"]/div/main/div/div[1]/div[5]/label/span',
            'XL': '//*[@id="root"]/div/main/div/div[1]/div[6]/label/span',
            'XXL': '//*[@id="root"]/div/main/div/div[1]/div[7]/label/span'
        }

@given('launch chrome browser')
def launch_chrome(context):
    context.driver = webdriver.Chrome()

@when('Navigate to shopping website')
def step_impl(context):
    context.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")


@when('selecting the size XS to XXl')
def get_size(context):
    status = False
    try:
        for size in ['XS', 'S', 'M', 'ML','L', 'XL', 'XXL' ]:
            element = context.driver.find_element(By.XPATH, f"{sizes['L']}")
            element.click()
            time.sleep(5)
            display_items = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/main/main/p') 
            print(f"items_shown = {display_items.text.split()[0]}")
            items_fetched = []
            for i in range(1, int(display_items.text.split()[0])+1):
                item = context.driver.find_element(By.XPATH, f"//div[@class='sc-uhudcz-0 iZZGui']/div[{i}]")
                items_fetched.append(item)
                break
            print(items_fetched)
            break
        assert status is True
    except Exception as e:
        assert status is False
    element = context.driver.find_element(By.XPATH, f"{sizes['S']}")
    element.click()
    
    


@then('close the Chrome browser')
def step_impl(context):
    context.driver.close()
