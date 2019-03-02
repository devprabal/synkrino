#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:48:51 2019

@author: devpogi
"""
from selenium import webdriver
browser = webdriver.Firefox(executable_path="geckodriver-v0.24.0-linux64/geckodriver")
browser.get("https://www.google.com")

