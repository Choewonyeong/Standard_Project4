from selenium import webdriver
from driver import RunDriver

searchList = ['화재', '원전', '소방', '원자력']
for idx, searchText in enumerate(searchList):
    RunDriver(idx, searchText)


