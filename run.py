import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


def SetChromePath():
    try:
        return './chromedriver_1.exe'
    except:
        pass
    try:
        return './chromedriver_2.exe'
    except:
        pass
    try:
        return './chromedriver_3.exe'
    except:
        pass


def run():
    try:
        searchTexts = ['화재', '원전', '소방', '원자력']

        CHROME_PATH = SetChromePath()

        chromeOptions = Options()
        chromeOptions.add_argument('--start-maximized')

        driver = webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=chromeOptions)

        tabs = driver.window_handles

        # idx, searchText
        for idx, searchText in enumerate(searchTexts):
            if not idx:
                driver.get('http://www.g2b.go.kr:8101/ep/tbid/tbidFwd.do')
            else:
                driver.execute_script('window.open("about:blank", "_blank");')
                driver.switch_to_window(tabs[0])

                taskDict = {'용역': 'taskClCds5'}
                checkbox = driver.find_element_by_id(taskDict['용역'])
                checkbox.click()

                # 검색어
                bidNm = driver.find_element_by_id('bidNm')
                bidNm.clear()
                bidNm.send_keys(searchText)
                bidNm.send_keys(Keys.RETURN)

                # 검색 조건
                optionDict = {'검색기간 한 달': 'setMonth1_1',
                              '입찰마감건 제외': 'exceptEnd',
                              '검색건수 표시': 'useTotalCount'}
                for option in optionDict.values():
                    checkbox = driver.find_element_by_id(option)
                    checkbox.click()

                # 목록 수 100건 선택
                recordCountPerPage = driver.find_element_by_name('recordCountPerPage')
                selector = Select(recordCountPerPage)
                selector.select_by_value('100')

                # 검색 버튼 클릭
                searchButton = driver.find_element_by_class_name('btn_mdl')
                searchButton.click()

                # 검색 결과 확인
                elements = driver.find_element_by_class_name('results')
                divList = elements.find_elements_by_tag_name('div')
    except:
        pass

run()
