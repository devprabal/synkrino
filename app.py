from flask import Flask, render_template, request
import time
import json
import threading
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
#from selenium.webdriver.common.alert import Alert
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
app = Flask(__name__)


my_dict = {}


def get_amazon_price(prod_id):
    prod_id = int(prod_id[4:])
    with open('products.json') as json_file:
        detailed_prod_dict = json.load(json_file)
    url_amazon = detailed_prod_dict['amazon'][prod_id-1]['amazon_url']
    if url_amazon!='':
        try:
            start_time_amazon = time.time()
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference('permissions.default.image', 2)
            firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
            options = Options()
            options.add_argument('-headless')
            capa = DesiredCapabilities.FIREFOX
            capa["pageLoadStrategy"] = "none"

            browser_amazon = webdriver.Firefox(executable_path="geckodriver-v0.24.0-linux64/geckodriver",options=options, desired_capabilities=capa, firefox_profile=firefox_profile)
            # url_amazon='https://www.amazon.in/Samsung-Galaxy-SM-G975FZKDINS-Black-Storage/dp/B07KXC7WQZ'
            browser_amazon.get(url_amazon)

            wait = WebDriverWait(browser_amazon, timeout=20)
            wait.until(expected.visibility_of_element_located((By.ID, 'priceblock_ourprice')))

            browser_amazon.execute_script("window.stop();")

        #    print(browser_amazon.page_source)

            amazon_price = browser_amazon.find_element_by_id("priceblock_ourprice").text
            amazon_price = '\u20B9'+str(amazon_price)
            browser_amazon.quit()
            end_time_amazon = time.time()
            price_and_delay = [amazon_price, end_time_amazon-start_time_amazon]
            my_dict['Samsung S10 Amazon'] = price_and_delay
            my_dict['Samsung S10 Amazon_url'] = url_amazon
        except TimeoutException:
            price_and_delay = ["Takes too long, try again or click buy now to view product's webpage", 'maybe internet issues']
            my_dict['Samsung S10 Amazon'] = price_and_delay
            my_dict['Samsung S10 Amazon_url'] = url_amazon
    else:
        price_and_delay = ["Product not available", '']
        my_dict['Samsung S10 Amazon'] = price_and_delay
        my_dict['Samsung S10 Amazon_url'] = url_amazon




def get_flipkart_price(prod_id):
    prod_id = int(prod_id[4:])
    with open('products.json') as json_file:
        detailed_prod_dict = json.load(json_file)
    url_flipkart = detailed_prod_dict['flipkart'][prod_id-1]['flipkart_url']
    if url_flipkart!='':
        try:
            start_time_flipkart = time.time()
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference('permissions.default.image', 2)
            firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
            options = Options()
            options.add_argument('-headless')
            capa = DesiredCapabilities.FIREFOX
            capa["pageLoadStrategy"] = "none"
            browser_flipkart = webdriver.Firefox(executable_path="geckodriver-v0.24.0-linux64/geckodriver",options=options, desired_capabilities=capa, firefox_profile=firefox_profile)
            # url_flipkart = 'https://www.flipkart.com/samsung-galaxy-s10-prism-black-128-gb/p/itmfdyp6fjtxf4hv?pid=MOBFDNHAXFKU9MHA'
            browser_flipkart.get(url_flipkart)

            wait = WebDriverWait(browser_flipkart, timeout=20)
            wait.until(expected.visibility_of_element_located((By.XPATH, "//div[@class='_1vC4OE _3qQ9m1']")))

            browser_flipkart.execute_script("window.stop();")

        #    print(browser_flipkart.page_source)

            # flipkart_price = browser_flipkart.find_element_by_class_name("_1vC4OE _3qQ9m1").text
            flipkart_price = browser_flipkart.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text
            # flipkart_price = '\u20B9'+str(flipkart_price)
            browser_flipkart.quit()
            end_time_flipkart = time.time()
            price_and_delay = [flipkart_price, end_time_flipkart-start_time_flipkart]
            my_dict['Samsung S10 Flipkart'] = price_and_delay
            my_dict['Samsung S10 Flipkart_url'] = url_flipkart
        except TimeoutException:
            price_and_delay = ["Takes too long, try again or click buy now to view product's webpage", 'maybe internet issues']
            my_dict['Samsung S10 Flipkart'] = price_and_delay
            my_dict['Samsung S10 Flipkart_url'] = url_flipkart
    else:
        price_and_delay = ["Product not available", '']
        my_dict['Samsung S10 Amazon'] = price_and_delay
        my_dict['Samsung S10 Amazon_url'] = url_flipkart
    



# This is a prototype..


def get_paytm_mall_price(prod_id):
    prod_id = int(prod_id[4:])
    with open('products.json') as json_file:
        detailed_prod_dict = json.load(json_file)
    url_paytm_mall = detailed_prod_dict['paytm_mall'][prod_id -1]['paytm_mall_url']
    if url_paytm_mall!='':
        try:
            start_time_paytm_mall = time.time()
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference('permissions.default.image', 2)
            firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
            options = Options()
            options.add_argument('-headless')
            capa = DesiredCapabilities.FIREFOX
            capa["pageLoadStrategy"] = "none"

            browser_paytm_mall = webdriver.Firefox(executable_path="geckodriver-v0.24.0-linux64/geckodriver",options=options, desired_capabilities=capa, firefox_profile=firefox_profile)
            # url_paytm_mall='https://paytmmall.com/samsung-galaxy-s10+-8-gb-512-gb-ceramic-black-MOBSAMSUNG-GALAHARD4002272BD4925-pdp?product_id=234393642&src=search-grid&tracker=organic%7C66781%7Csamsung%20galaxy%20s10%7Cgrid%7CSearch_experimentName%3Dnew_ranking%7C%7C2%7Cnew_ranking&site_id=2&child_site_id=6'
            browser_paytm_mall.get(url_paytm_mall)

            wait = WebDriverWait(browser_paytm_mall, timeout=20)
            wait.until(expected.visibility_of_element_located((By.CLASS_NAME, '_1V3w')))

            browser_paytm_mall.execute_script("window.stop();")

        #    print(browser_amazon.page_source)

            paytm_mall_price = browser_paytm_mall.find_element_by_class_name("_1V3w").text
            paytm_mall_price = '\u20B9'+str(paytm_mall_price)
            browser_paytm_mall.quit()
            end_time_paytm_mall = time.time()
            price_and_delay = [paytm_mall_price,end_time_paytm_mall-start_time_paytm_mall]
            my_dict['Samsung S10 PaytmMall'] = price_and_delay
            my_dict['Samsung S10 PaytmMall_url'] = url_paytm_mall
        except TimeoutException:
            price_and_delay = ["Takes too long, try again or click buy now to view product's webpage", 'maybe internet issues']
            my_dict['Samsung S10 PaytmMall'] = price_and_delay
            my_dict['Samsung S10 PaytmMall_url'] = url_paytm_mall
    else:
        price_and_delay = ["Product not available", '']
        my_dict['Samsung S10 Amazon'] = price_and_delay
        my_dict['Samsung S10 Amazon_url'] = url_paytm_mall


# End of prototype..


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/hello/<prod_id>', methods=['POST'])


@app.route('/hello')
def hello():
    prod_id = request.args.get('prod_id', None)
    main_start_time = time.time()
    t1 = threading.Thread(target=get_amazon_price, args=(prod_id,))
    t2 = threading.Thread(target=get_flipkart_price, args=(prod_id,))
    t3 = threading.Thread(target=get_paytm_mall_price, args=(prod_id,))
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # wait until thread 3 is completely executed
    t3.join()

    # for Samsung S10
    # search_item = request.form['search_item_field']
#    options = Options()
#    options.add_argument('-headless')
#    driver = webdriver.Firefox(executable_path='geckodriver', options=options)
#    wait = WebDriverWait(driver, timeout=10)

#    firefox_profile = webdriver.FirefoxProfile()
#    firefox_profile.set_preference('permissions.default.image', 2)
#    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
#    browser_amazon = webdriver.Firefox(firefox_profile=firefox_profile,options=options)
#    capa = DesiredCapabilities.FIREFOX
#    capa["pageLoadStrategy"] = "none"
#
#
#    browser_amazon = webdriver.Firefox(options=options,desired_capabilities=capa)
#    url_amazon='https://www.amazon.in/Samsung-Galaxy-SM-G975FZKDINS-Black-Storage/dp/B07KXC7WQZ'
#    start_time_amazon = time.time()
#    browser_amazon.get(url_amazon)
#
#    wait = WebDriverWait(browser_amazon, timeout=20)
#    wait.until(expected.visibility_of_element_located((By.ID, 'priceblock_ourprice')))
#
#    browser_amazon.execute_script("window.stop();")
#
#    print(browser_amazon.page_source)
#
#    amazon_price = browser_amazon.find_element_by_id("priceblock_ourprice").text
#    browser_amazon.quit()
#    end_time_amazon = time.time()

    # search_bar.clear()
    # search_bar.send_keys(search_item)
    # search_bar.send_keys(Keys.RETURN)
    # WebDriverWait(browser,8).until(EC.presence_of_element_located((By.ID,'result_0')))
    # price_0_field = browser.find_element_by_xpath("//span[@class='a-size-base a-color-price a-text-bold']/text()")
    # price_0 = price_0_field.text
#    browser_flipkart = webdriver.Firefox(firefox_profile=firefox_profile,options=options)
#    browser_flipkart = webdriver.Firefox(options=options,desired_capabilities=capa)
#    url_flipkart = 'https://www.flipkart.com/samsung-galaxy-s10-prism-black-128-gb/p/itmfdyp6fjtxf4hv?pid=MOBFDNHAXFKU9MHA'
#    start_time_flipkart = time.time()
#    browser_flipkart.get(url_flipkart)
#
#
#    wait = WebDriverWait(browser_flipkart, timeout=20)
#    wait.until(expected.visibility_of_element_located((By.XPATH, "//div[@class='_1vC4OE _3qQ9m1']")))
#
#    browser_flipkart.execute_script("window.stop();")
#
#    print(browser_flipkart.page_source)
#
#    # flipkart_price = browser_flipkart.find_element_by_class_name("_1vC4OE _3qQ9m1").text
#    flipkart_price = browser_flipkart.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text
#    browser_flipkart.quit()
#    end_time_flipkart = time.time()

    main_end_time = time.time()
#    return 'Amazon %s timetaken- %s<br/>Flipkart %s timetaken- %s<br/>Main execution time = %s <br/> <a href="/">Back Home</a>' % (my_dict['Samsung S10 Amazon'][0], my_dict['Samsung S10 Amazon'][1], my_dict['Samsung S10 Flipkart'][0], my_dict['Samsung S10 Flipkart'][1],main_end_time-main_start_time )
    # return render_template('price.html',amazon_price=my_dict['Samsung S10 Amazon'][0],flipkart_price=my_dict['Samsung S10 Flipkart'][0],paytm_mall_price=my_dict['Samsung S10 PaytmMall'][0],scraper_run_time=main_end_time-main_start_time)
    return render_template('price.html', scraper_run_time=main_end_time-main_start_time, amazon_price=my_dict['Samsung S10 Amazon'][0], amazon_url=my_dict['Samsung S10 Amazon_url'], flipkart_price=my_dict['Samsung S10 Flipkart'][0], flipkart_url=my_dict['Samsung S10 Flipkart_url'], paytm_mall_price=my_dict['Samsung S10 PaytmMall'][0], paytm_mall_url=my_dict['Samsung S10 PaytmMall_url'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
