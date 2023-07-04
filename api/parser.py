from bs4 import BeautifulSoup
import requests

def GetJGdates(year):
    result = [year]
    for hakgi in [1,2]:
        url = "https://registrar.korea.ac.kr/eduinfo/affairs/schedule.do?cYear="+str(year)+"&hakGi="+str(hakgi)
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        items = soup.select("#jwxe_main_content > div > div > div > div > div > table > tr")
        month = 0
        day = 0

        for item in items:
            ths = item.select("th")
            if len(ths) != 0:
                month = ths[0].select_one("span").get_text().strip()[0:-1]
            tds = item.select("td")
            if(tds[1].select_one("div").get_text() == "제"+str(hakgi)+"학기 개강"):
                temp = tds[0].get_text().strip()
                day = int(temp[0:temp.find('(')])
                result.append(f'{month}/{day}')
            if(tds[1].select_one("div").get_text()[2:7] == "방학 시작"):
                temp = tds[0].get_text().strip()
                day = int(temp[0:temp.find('(')])
                result.append(f'{month}/{day}')
    return result

        

