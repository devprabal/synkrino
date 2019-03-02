from flask import Flask, render_template, request
import time
import threading
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
#from selenium.webdriver.common.alert import Alert
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
app = Flask(__name__)


my_dict = {}
def get_amazon_price():
    start_time_amazon = time.time()
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    options = Options()
    options.add_argument('-headless')
    capa = DesiredCapabilities.FIREFOX
    capa["pageLoadStrategy"] = "none"

    
    browser_amazon = webdriver.Firefox(options=options,desired_capabilities=capa, firefox_profile=firefox_profile)
    url_amazon='https://www.amazon.in/Samsung-Galaxy-SM-G975FZKDINS-Black-Storage/dp/B07KXC7WQZ'
    browser_amazon.get(url_amazon)
    
    wait = WebDriverWait(browser_amazon, timeout=20)
    wait.until(expected.visibility_of_element_located((By.ID, 'priceblock_ourprice')))
    
    browser_amazon.execute_script("window.stop();")
    
#    print(browser_amazon.page_source)
    
    amazon_price = browser_amazon.find_element_by_id("priceblock_ourprice").text
    browser_amazon.quit()
    end_time_amazon = time.time()
    price_and_delay = [amazon_price,end_time_amazon-start_time_amazon]
    my_dict['Samsung S10 Amazon']=price_and_delay



def get_flipkart_price():
    start_time_flipkart = time.time()
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    options = Options()
    options.add_argument('-headless')
    capa = DesiredCapabilities.FIREFOX
    capa["pageLoadStrategy"] = "none"
    browser_flipkart = webdriver.Firefox(options=options,desired_capabilities=capa,firefox_profile=firefox_profile)
    url_flipkart = 'https://www.flipkart.com/samsung-galaxy-s10-prism-black-128-gb/p/itmfdyp6fjtxf4hv?pid=MOBFDNHAXFKU9MHA'
    browser_flipkart.get(url_flipkart)
    
    
    wait = WebDriverWait(browser_flipkart, timeout=20)
    wait.until(expected.visibility_of_element_located((By.XPATH, "//div[@class='_1vC4OE _3qQ9m1']")))
    
    browser_flipkart.execute_script("window.stop();")
    
#    print(browser_flipkart.page_source)
    
    # flipkart_price = browser_flipkart.find_element_by_class_name("_1vC4OE _3qQ9m1").text
    flipkart_price = browser_flipkart.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text
    browser_flipkart.quit()
    end_time_flipkart = time.time()
    price_and_delay = [flipkart_price,end_time_flipkart-start_time_flipkart]
    my_dict['Samsung S10 Flipkart']=price_and_delay




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    
    main_start_time = time.time()
    t1 = threading.Thread(target=get_amazon_price) 
    t2 = threading.Thread(target=get_flipkart_price) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
    
    
    
    
    
    
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
    return render_template('price.html',amazon_price=my_dict['Samsung S10 Amazon'][0],flipkart_price=my_dict['Samsung S10 Flipkart'][0],scraper_run_time=main_end_time-main_start_time)





if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
