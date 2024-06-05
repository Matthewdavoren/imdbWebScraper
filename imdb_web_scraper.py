from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import csv
import time

options = webdriver.FirefoxOptions()
options.add_argument("--headless") 

service = FirefoxService(executable_path="/usr/local/bin/geckodriver")

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.imdb.com/chart/top")

time.sleep(5)

movies = driver.find_elements(By.CSS_SELECTOR, 'tbody.lister-list tr')

with open('imdb_top_250_movies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Year', 'Rating'])

    for movie in movies:
        title = movie.find_element(By.CSS_SELECTOR, '.titleColumn a').text
        year = movie.find_element(By.CSS_SELECTOR, '.titleColumn span').text.strip('()')
        rating = movie.find_element(By.CSS_SELECTOR, '.imdbRating strong').text
        
        writer.writerow([title, year, rating])

print("Scraping completed and data saved to imdb_top_250_movies.csv")
driver.quit()


