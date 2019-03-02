#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
from selenium import webdriver
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://www.flipkart.com/samsung-galaxy-s10-prism-black-128-gb/p/itmfdyp6fjtxf4hv?pid=MOBFDNHAXFKU9MHA')

#firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.add_extension('' + "image_block-5.0-fx.xpi")
#firefox_profile.set_preference("ima")
#browser = webdriver.Firefox()
#browser.install_addon('/home/devpogi/Documents/synkrino/' + "image_block-5.0-fx.xpi", temporary=True)
#
#
##driver = webdriver.Firefox(firefox_profile)
#browser.get('https://www.flipkart.com/samsung-galaxy-s10-prism-black-128-gb/p/itmfdyp6fjtxf4hv?pid=MOBFDNHAXFKU9MHA')
#browser.close()
