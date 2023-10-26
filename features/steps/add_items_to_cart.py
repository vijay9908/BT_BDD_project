from behave import *
import time, random
from selenium import webdriver
from helpers import find_intersection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

data = {'Cropped Stay Groovy off white': 1,
        'Basic Cactus White T-shirt': 2,
        'Skater Black Sweatshirt': 3,
        'Black Tule Oversized': 4,
        'Black Batman T-shirt': 5,
        'Blue T-Shirt': 6,
        'Loose Black T-shirt': 7,
        'Ringer Hall Pass': 8,
        'Grey T-shirt': 9,
        'Black T-shirt with white stripes': 10,
        'Turtles Ninja T-shirt': 11,
        'Slim black T-shirt': 12,
        'Blue Sweatshirt': 13,
        'White T-shirt Gucci': 14,
        'Tropical Wine T-shirt': 15,
        'Marine Blue T-shirt': 16,
    }

free_ship_items = None
non_free_ship_items = None

@when('Add random 4 items into cart with free shipping and one without')
def Add_items_with_and_without_free_shipping(context):
    time.sleep(3)
    display_items = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/main/main/p') 
    display_items = int(display_items.text.split()[0])

    items_picked = {}
    non_ship_items = {}

    while len(items_picked) < 4:
        random_id = random.randint(1, display_items)
        try:
            label_field = context.driver.find_element(By.XPATH, f"//*[@id='root']/div/main/main/div/div[{random_id}]/div[1]")
            
            if not items_picked.get(random_id) and label_field.text:
                price = context.driver.find_element(By.XPATH, f"//*[@id='root']/div/main/main/div/div[{random_id}]/div[3]/p[1]")
                items_picked[random_id] = price.text
                time.sleep(2)
                add_to_cart_btn = context.driver.find_element(By.XPATH, f"//*[@id='root']/div/main/main/div/div[{random_id}]/button")
                time.sleep(2)
                add_to_cart_btn.click()
            else:
                continue
        except Exception as e:
            continue

    got_item = False
    while not got_item:
        random_id = random.randint(1, display_items)
        try:
            label_field = context.driver.find_element(By.XPATH, f"//*[@id='root']/div/main/main/div/div[{random_id}]/div[1]")
        except Exception as e:
            pass
        if not items_picked.get(random_id) and not label_field.text:
            price = context.driver.find_element(By.XPATH, f"//*[@id='root']/div/main/main/div/div[{random_id}]/div[2]/p[1]") 
            non_ship_items[random_id] = price.text
            time.sleep(1)
            add_to_cart_btn = context.driver.find_element(By.XPATH, f"//*[@id='root']/div/main/main/div/div[{random_id}]/button")
            time.sleep(2)
            add_to_cart_btn.click()
            got_item = True
                
    global free_ship_items
    global non_free_ship_items
    free_ship_items = items_picked
    non_free_ship_items = non_ship_items

@when('Verify cart post adding items')
def verify_cart(context):
    cart_size = int(context.driver.find_element(By.XPATH, '//div[@class="sc-1h98xa9-3 VLMSP"]').get_attribute('innerHTML'))
    cart_items = find_intersection(free_ship_items, non_free_ship_items)
    for item in range(1, cart_size+1):
        item_div = context.driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[2]/div/div[2]/div[{item}]') 
        # print(data[item_div.text.split('\n')[0]])
    
    total_items_data = {**free_ship_items, **non_free_ship_items}
    assert cart_items == total_items_data
