from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Config:

    serv_obj=Service("C:/Users/ABC/Documents/Web Drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
