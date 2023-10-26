from behave import *
import time
from selenium import webdriver
from helpers import click_element, beautify_data, find_intersection
from validation_data import get_data_to_verify, get_validation_data_for_size_S_and_M
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

sizes = {
            "XS": "//span[normalize-space()='XS']", 
            "S":  "//span[normalize-space()='S']",
            "M":  "//span[normalize-space()='M']",
            "ML": "//span[normalize-space()='ML']", 
            "L":  "//span[normalize-space()='L']",  
            "XL": "//span[normalize-space()='XL']",
            "XXL": "//span[normalize-space()='XXL']"
        }

polled_page_data = None

@given('launch chrome browser')
def launch_chrome(context):
    context.driver = webdriver.Chrome()

@when('Navigate to shopping website')
def step_impl(context):
    context.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")

@when('Poll data of all sizes from Website')
def get_size(context):
    page_data_wrt_sizes = {}
    status = False
    try:
        for size in ['XS', 'S', 'M', 'ML', 'L', 'XL', 'XXL']:
            # to select the size
            element = context.driver.find_element(By.XPATH, f"{sizes[size]}")
            element.click()
            time.sleep(2)
            display_items = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/main/main/p') 
            
            items_fetched = []
            for i in range(1, int(display_items.text.split()[0])+1):
                item = context.driver.find_element(By.XPATH, f"//div[@class='sc-uhudcz-0 iZZGui']/div[{i}]")
                items_fetched.append(item.text)
            
            page_data_wrt_sizes[size] = beautify_data(items_fetched)

            # to un-select the selected size
            element = context.driver.find_element(By.XPATH, f"{sizes[size]}")
            element.click()
            time.sleep(2)

        global polled_page_data
        polled_page_data = page_data_wrt_sizes
        # print(polled_page_data)

        assert status is True
    except Exception as e:
        assert status is False

@when("Selecting the entered size {said_size} and validating data")
def step_impl(context, said_size):
    if said_size == 'All':
        fetched_data = polled_page_data
        validation_data = get_data_to_verify(said_size, get_all=True)
    else:
        fetched_data = polled_page_data[said_size]
        validation_data = get_data_to_verify(said_size)

    assert fetched_data == validation_data, f"Size validation for size: {said_size} failed"

@when("Validating combined filters of provided sizes {sizes}")
def step_impl(context, sizes):
    try:
        validation_data = get_validation_data_for_size_S_and_M()
        filtered_data = {}
        size_S = polled_page_data['S']
        size_M = polled_page_data['M']
        compute_data = find_intersection(size_S, size_M)
        print(compute_data, validation_data)
        assert compute_data == validation_data, "Validating combined filters of provided sizes S and M not matching"
    except Exception as e:
        assert False, "Validating combined filters of provided sizes S and M is invalid"
    
@then('close the Chrome browser')
def step_impl(context):
    context.driver.close()

