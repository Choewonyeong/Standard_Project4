from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import datetime
import time
import os
print('start')
times = 20
while True:
    if str(datetime.datetime.now())[11:13] == '10':

        times = 20
        print(times)
        #if not (str(datetime.datetime.now())[0:10].replace('-', '') + '.csv' in os.listdir('bin')):
        if True:
            times = 50
            print(times)
            driver = webdriver.Chrome('./chromedriver_1')
            results = []
            querylist = ['홈페이지', '플랫폼', '포털', '시스템', '구축', '빅데이터', '산학협력', '산학포털', 'LINC', '업무지원', '평생교육', '솔루션']
            querylist2 = ['중앙신체검사소', '한국감정원', '한국교육학술정보원', '한국산업단지공단', '한국사학진흥재단', '한국산업기술평가관리원', '한국가스공사', '신용보증기금',
                          '중앙119구조본부', '한국정보화진흥원', '중앙교육연수원', '한국장학재단', '대구경북첨단의료산업진흥재단', '의료기술시험훈련원', '한국뇌연구원',
                          '한의기술응용센터', '한국도로공사', '한국건설관리공사', '교통안전공단', '국립농산물품질관리원', '농림축산검역본부', '국립종자원', '한국전력기술',
                          '대한법률구조공단', '우정사업조달사무소', '기상통신소', '조달품질원', '한국법무보호복지공단', '에너지경제연구원', '근로복지공단', '노동부고객상담센터',
                          '한국산업인력공단', '한국산업안전보건공단', '국립재난안전연구원', '한국동서발전', '한국석유공사', '한국에너지공단', '한국토지주택공사', '주택관리공단',
                          '한국시설안전공단', '중소기업진흥공단', '한국산업기술시험원', '한국세라믹기술원', '한국남동발전', '한국승강기안전관리원', '국방기술품질원', '중앙관세분석소',
                          '한국저작권위원회', '대구광역시', '대구광역시교육청', '대구광역시교육연구정보원', '경상북도교육청', '경상북도교육연구원', '경상북도교육정보센터',
                          '국립대구과학관']
            n = len(querylist) * len(querylist2)
            t = 0
            try:
                for query in querylist:
                    for query2 in querylist2:
                        t = t + 1
                        driver.get('http://www.g2b.go.kr:8101/ep/tbid/tbidFwd.do')

                        # 업무 종류 체크
                        #            task_dict = {'용역': 'taskClCds5', '민간': 'taskClCds20', '기타': 'taskClCds4'}
                        #            for task in task_dict.values():
                        #                checkbox = driver.find_element_by_id(task)
                        #                checkbox.click()

                        instNm = driver.find_element_by_id('instNm')
                        instNm.clear()
                        instNm.send_keys(query2)
                        instNm.send_keys(Keys.RETURN)
                        # 입찰정보 검색 페이지로 이동

                        # 검색어
                        # id값이 bidNm인 태그 가져오기
                        bidNm = driver.find_element_by_id('bidNm')
                        # 내용을 삭제 (버릇처럼 사용할 것!)
                        bidNm.clear()
                        # 검색어 입력후 엔터
                        bidNm.send_keys(query)
                        bidNm.send_keys(Keys.RETURN)
                        # 검색 조건 체크
                        option_dict = {'검색기간 1달': 'setMonth1_1', '입찰마감건 제외': 'exceptEnd'}
                        for option in option_dict.values():
                            checkbox = driver.find_element_by_id(option)
                            checkbox.click()
                        # 목록수 100건 선택 (드롭다운)
                        recordcountperpage = driver.find_element_by_name('recordCountPerPage')
                        selector = Select(recordcountperpage)
                        selector.select_by_value('100')
                        # 검색 버튼 클릭
                        search_button = driver.find_element_by_class_name('btn_mdl')
                        search_button.click()
                        # 검색 결과 확인
                        elem = driver.find_element_by_class_name('results')
                        div_list = elem.find_elements_by_tag_name('div')
                        # 검색 결과 모두 긁어서 리스트로 저장
                        # results.append(query)
                        # if len(div_list)!=0:
                        #    results.append(query)
                        for div in div_list:
                            results.append(div.text)
                            a_tags = div.find_elements_by_tag_name('a')
                            if a_tags:
                                for a_tag in a_tags:
                                    link = a_tag.get_attribute('href')
                                    results.append(link)
                        # 검색결과 모음 리스트를 12개씩 분할하여 새로운 리스트로 저장
                        # result = [results[i * 13:(i + 1) * 13] for i in range((len(results) + 13 - 1) // 13 )]
                        result = [results[i * 12:(i + 1) * 12] for i in range((len(results) + 12 - 1) // 12)]
                        # 결과 출력
                        print(round(t / n * 100, 2))
                        # print(result)
            except Exception as e:
                # 위 코드에서 에러가 발생한 경우 출력
                print(e)
            finally:
                # 에러와 관계없이 실행되고, 크롬 드라이버를 종료
                driver.quit()

            my_df = pd.DataFrame(result)
            my_df.to_csv('bin/test.csv', index=False, header=False, encoding='cp949')
            my_df.to_csv('bin/' + str(datetime.datetime.now())[0:10].replace('-', '') + '.csv', index=False,
                         header=False, encoding='cp949')
    time.sleep(60 * times)