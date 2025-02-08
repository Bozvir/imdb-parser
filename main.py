from bs4 import BeautifulSoup
import lxml, csv, re, requests
from selenium import webdriver
import time
final_list=[]
final_list.append(["Place and name","Year", "Rating", "Number of Ratings", "URL"])

options = webdriver.ChromeOptions()
options.add_argument("--lang=en-US")
driver = webdriver.Chrome(options=options)
url="https://www.imdb.com/chart/top/"

driver.get(url)
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "lxml")

metadata=re.compile("cli-title-metadata-item")

film_card=soup.find_all("li", class_="ipc-metadata-list-summary-item")
for item in film_card:
    place_and_name = item.find("h3", class_="ipc-title__text").text.strip()

    film_year=item.find("span",class_=metadata).text.strip()

    rating=item.find("span", class_="ipc-rating-star--rating").text.strip()
    number_of_ratings=item.find("span", class_="ipc-rating-star--voteCount").text.strip()
    clean_number_of_ratings=number_of_ratings.replace("\xa0", "").strip("()В")

    url=item.find("a")
    film_url=url.get("href")

    final_list.append([place_and_name.strip(), film_year.strip(), rating.strip(), clean_number_of_ratings.strip(), "https://imdb.com" + film_url.strip()])

driver.quit()
with open("final_list.csv", "w", encoding="utf8") as final_file:
    writer=csv.writer(final_file, lineterminator='\n')
    for data in final_list:
        writer.writerow(data)

