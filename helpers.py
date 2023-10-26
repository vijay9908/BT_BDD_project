from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

def click_element(element, wait=None):
    if time:
        time.sleep(wait)
    element.click()
    

total_items = ['Free shipping\nCropped Stay Groovy off white\n$10.90\nor 9 x$1.21\nAdd to cart', 'Free shipping\nBasic Cactus White T-shirt\n$13.25\nor 3 x$4.42\nAdd to cart', 'Skater Black Sweatshirt\n$25.90\nor 12 x$2.16\nAdd to cart', 'Free shipping\nBlack Tule Oversized\n$29.45\nor 5 x$5.89\nAdd to cart', 'Free shipping\nBlack Batman T-shirt\n$10.90\nor 9 x$1.21\nAdd to cart', 'Free shipping\nBlue T-Shirt\n$9.00\nor 3 x$3.00\nAdd to cart', 'Free shipping\nLoose Black T-shirt\n$14.00\nor 5 x$2.80\nAdd to cart', 'Free shipping\nRinger Hall Pass\n$10.90\nor 9 x$1.21\nAdd to cart', 'Free shipping\nGrey T-shirt\n$14.90\nor 7 x$2.13\nAdd to cart', 'Free shipping\nBlack T-shirt with white stripes\n$14.90\nor 7 x$2.13\nAdd to cart', 'Turtles Ninja T-shirt\n$10.90\nor 9 x$1.21\nAdd to cart', 'Free shipping\nSlim black T-shirt\n$49.90\nAdd to cart', 'Free shipping\nBlue Sweatshirt\n$22.50\nor 4 x$5.63\nAdd to cart', 'White T-shirt Gucci\n$18.70\nor 4 x$4.67\nAdd to cart', 'Free shipping\nTropical Wine T-shirt\n$134.90\nor 5 x$26.98\nAdd to cart', 'Free shipping\nMarine Blue T-shirt\n$49.00\nor 9 x$5.44\nAdd to cart']

def beautify_data(raw_data, size=None):
    res = {}
    for ele in raw_data:
        data = ele
        item = data.split('\n')
        shipping_cost = 'Not Free' if len(item) == 4 else 'Free shipping'
        name = item[1]
        single_cost = item[2]
        bunch_string = item[3].split()
        bunch_quantity, bunch_cost = bunch_string[1], bunch_string[2]
        res[name] = [shipping_cost, name, single_cost, bunch_quantity, bunch_cost]
        if size:
            res[name].append(size)
    return res

def find_intersection(raw_data1, raw_data2):
    intersection = {**raw_data1, **raw_data2}
    return intersection

# res1 = {'Black Batman T-shirt': ['Free shipping', 'Black Batman T-shirt', '$10.90', '9', 'x$1.21'], 'Blue Sweatshirt': ['Free shipping', 'Blue Sweatshirt', '$22.50', '4', 'x$5.63']}
# res2 = {'Black Tule Oversized': ['Free shipping', 'Black Tule Oversized', '$29.45', '5', 'x$5.89']}

# print(find_intersection(res1, res2))
