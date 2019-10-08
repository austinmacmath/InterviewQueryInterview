from bs4 import BeautifulSoup
import requests
from time import sleep, time
from random import randint
import numpy as np
import pandas as pd

def main():
    # class for creating objects of type Question
    class Question():
        def __init__(self, company, question, answers, date_created, position_title):
            self.company = company
            self.question = question
            self.answer = answer
            self.date_created = date_created
            self.position_title = position_title

    # specify User-Agent to circumvent bot detection
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    # counter for number of listings
    i = 0
    start_time = time()


    # create empty DataFrame for data
    df = pd.DataFrame(columns = ["Company", "Question", "Answers", "Date Created", "Position Title"])

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
            current_time = time()
            elapsed_time = current_time - start_time
            
            # exception handling
            try:
                if listing.find("p", class_ = "cell noMargVert padTop tightBot") is not None:
                    answer = listing.find("p", class_ = "cell noMargVert padTop tightBot").text
                else:
                    answer = ""

                question = listing.find("p", class_ = "questionText h3").text
                date = listing.find("div", class_ = "cell alignRt noWrap minor hideHH").text
                position_company = listing.find("span", class_ = "authorInfo").text

                # selects substring of position title
                start_position = 0
                end_position = position_company.index(" at ")
                position = position_company[start_position: end_position]

                # selects substring of company
                start_company = position_company.index(" at ") + 4
                end_company = position_company.index(" was asked...")
                company = position_company[start_company: end_company]

                # initialize question object with scraped data
                q1 = Question(company, question, answer, date, position)

                # insert into DataFrame
                df2 = pd.DataFrame({"Company": [q1.company], "Question": [q1.question], "Answers": [q1.answer], "Date Created": [q1.date_created], "Position Title": [q1.position_title]})
                df = df.append(df2, ignore_index = True)

                # reset class variables
                q1 = Question("", "", "", "", "")

                print('Listing: {}; Frequency: {} listings/s'.format(i, i/elapsed_time))
            except UnicodeEncodeError:
                print("UnicodeEncodeError")

        # stop once we have over 100 listings
        if i >= 100:
            break

    # save DataFrame as CSV
    df.to_csv("GlassdoorData.csv")

if __name__ == "__main__":
    main()
