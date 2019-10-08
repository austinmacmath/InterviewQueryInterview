from bs4 import BeautifulSoup
import requests
from time import sleep, time
from random import randint

class question():
    def __init__(self, ):


# specify User-Agent to circumvent bot detection
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# counter for number of listings
i = 0

# scrapes pages 1-19
for page in range(1,20):
    url = 'https://www.glassdoor.com/Interview/data-scientist-interview-questions-SRCH_KO0,14_SDRD_IP' + str(page) + '.htm'
    page = requests.get(url, headers=agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    listings = soup.find_all("div", class_ = "interviewQuestion noPad")

    # randomizes time between requests to prevent getting blocked
    sleep(randint(1, 3))

    # scrapes every listing on each page
    for listing in listings:
        i += 1
        
        # exception handling
        try:
            if listing.find("p", class_ = "cell noMargVert padTop tightBot") is not None:
                answer = listing.find("p", class_ = "cell noMargVert padTop tightBot").text
            else:
                answer = ""
            position_company = listing.find("span", class_ = "authorInfo").text
            question = listing.find("p", class_ = "questionText h3").text
            date = listing.find("div", class_ = "cell alignRt noWrap minor hideHH").text
            print("{} . {} {} {} {}".format(str(i),date, position_company, question, answer))
        except UnicodeEncodeError:
            print("UnicodeEncodeError")

    if i >= 100:
        break

""" url = "https://www.glassdoor.com/Interview/data-scientist-interview-questions-SRCH_KO0,14_SDRD.htm"
headers = {'authority': 'www.glassdoor.com', 'method': 'GET', 'path': '/Interview/data-scientist-interview-questions-SRCH_KO0,14_SDRD.htm', 'scheme': 'https', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'cookie': 'gdId=f7e05e9b-c514-405a-b376-c1d879768bc9; G_ENABLED_IDPS=google; fbm_129253937150340=base_domain=.glassdoor.com; trs=indeed:indeed-indeed-slots-up:cpc:2019-10-03+20%3A52%3A18.91:undefined:undefined; __gdpopuc=1; JSESSIONID_JX_APP=47FA8E5D50F6C68342AF8F81EF0D1E55; GSESSIONID=C405916E1CBD41C9DA7162091C8225F1; uc=8F0D0CFA50133D96DAB3D34ABA1B8733E3AE1E692FFB19EB6FB967D7F86B91C6BAFD39AE85F73A074DF50234D18EB46494C4A8DDC075EEF25921B53A14F0E54F48303B05A47C095D458FFB19827900A5B8C546A5C57012C0A255F45C402B1D66094D4DAF8E510145032E1A094E9EA3C357C413C76B1AE3FD826BECF8D5E3CF7E8F95CD2C5C941CA438B757A53AB21615E551AFAA972DD904772CD939EDBDB8B8; JSESSIONID_KYWI_APP=BEEA73281E6579EACE399DEAF176960A; JSESSIONID=8408F12825E2BA16DE0EF6DC9C3B6992; __cf_bm=18c15707385c8c70bca42e1615d04cdfef6b9737-1570505301-1800-AYvo8B+OQ4CbKcODr3lxRkJEXp9/zq6FzKEmKZg7sZj90MhCurY+BAoTswxT3T1KLRTfoTaWWs/u02gkHQhrA8c=; cass=1; AWSALB=XvGU9qQ9QUjcXbTn2ykeP00u573p4IYAtAsZD/7t6ysYt30xdDCCWQEu3AXmPdJxPhIx/tJqo5RpC+mX1Arupwz6SX2Z5+IeU1OdNI1ej6b0dGu3CtnWGZK6Hbi0mzfPkSyCxuetLRfEA+lQPGy6m+aCeX1XnJBf/BQf+2fK9mkou6z7HdT0UekchJv0Ag==; _uac=0000016da96925b9aca312596bdc9c31', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, "html.parser")
print (soup.prettify()) """

#print soup.find("span", class_ = "authorInfo").text