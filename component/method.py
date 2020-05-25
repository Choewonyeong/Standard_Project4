from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pandas import DataFrame, ExcelWriter


def setDriver():
    try:
        driver = webdriver.Chrome('./chromedriver_1.')
        return driver
    except:
        pass

    try:
        driver = webdriver.Chrome('./chromedriver_2')
        return driver
    except:
        pass

    try:
        driver = webdriver.Chrome('./chromedriver_3')
        return driver
    except:
        pass


def runDriver(idx, searchText):
    driver = setDriver()
    driver.get('http://www.g2b.go.kr:8101/ep/tbid/tbidFwd.do')
