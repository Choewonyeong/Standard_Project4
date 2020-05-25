from selenium import webdriver


def SetDriver():
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


def RunDriver(idx, searchText):
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select

    driver = SetDriver()
    tabs = driver.window_handles

    try:
        # 입찰정보 검색
        driver.execute_script('window.open("about:blank", "_blank");')
        driver.switch_to_window(tabs[idx])
        driver.get('http://www.g2b.go.kr:8101/ep/tbid/tbidFwd.do')
        taskDict = {'용역': 'taskClCds5'}
        checkbox = driver.find_element_by_id(taskDict['용역'])
        checkbox.click()

        # 검색어
        query = searchText
        bidNm = driver.find_element_by_id('bidNm')
        bidNm.clear()
        bidNm.send_keys(query)
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

        # 검색 결과 저장
        results = []
        for div in divList:
            results.append(div.text)
            aTags = div.find_element_by_tag_name('a')
            print(aTags)
            if aTags:
                for aTag in aTags:
                    link = aTag.get_attribute('href')
                    results.append(link)
        print(results)

        result = [results[i * 12: (i + 1) * 12] for i in range((len(results) + 12 - 1) // 12)]
        print(result)

    except Exception as e:
        print(e)
        pass
    finally:
        pass
        # driver.quit()