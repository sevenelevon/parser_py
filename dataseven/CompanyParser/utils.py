import requests
import lxml
from bs4 import BeautifulSoup
import re

listLink = []
LinkCompanyList = []

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    }
    
    for count in range(3):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        
        name = soup.find("h1", class_="bloko-header-section-3").text
        name = name.strip()
        
        company = soup.find("h1", class_="bloko-header-section-3").text
        company = name.strip()
        
        linkBussinesStep1 = soup.find_all("div", class_="vacancy-serp-item-body__main-info")
        for i in linkBussinesStep1:
            link = i.find("a").get("href")
            listLink.append(link)
        
    # Парсинг ссылки
    
    for i in listLink:
        response = requests.get(i, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        try:
            linkBussinesStep2 = soup.find("span", class_="vacancy-company-name").find("a").get("href")
        except:
            print("Ссылка не валидная")
            continue
        LinkCompanyList.append(linkBussinesStep2)
        SearchActiveCompany = soup.find("div", class_="bloko-gap bloko-gap_bottom").find("p").text
        try:
            datePattern = re.compile(r"\b(\d{1,2})\s+(\w+)\s+(\d{4})\b")
            date = re.search(datePattern, SearchActiveCompany).group()
        except:
            print("Шаблон даты не совпадает")
            continue
    
    for i in LinkCompanyList:
        response = requests.get("https://spb.hh.ru" + i, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        
        try:
            NameCompany = soup.find("h1", class_="bloko-header-1").text
        except:
            print("Название компании не найдено")
            continue
        try:
            cityCompany = soup.find("div", class_="employer-sidebar-content").find("div", class_="employer-sidebar-block").text
        except:
            print("Город компании не найден")
            continue
        try: 
            SiteCompany = soup.find("div", class_="employer-sidebar-content").find("a").get("href")
        except:
            print("Сайт компании не найден")
            continue
        try: 
            ActivityCompany = soup.find("div", class_="employer-sidebar-content").find("p").text
        except:
            print("Деятельность компании не найдена")
            continue
        
        try:
            number_text = soup.get_text(strip=True)
            number = (re.findall("\d+" + "активных вакансий", number_text)[0])
            filterNumber = int(re.findall("\d+", number)[0])
            if filterNumber >= 5:
                notification = "Компания активно развивается"
        except:
            print()
            continue
        
    return name, company, date, NameCompany, cityCompany, SiteCompany, ActivityCompany, notification