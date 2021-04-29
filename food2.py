from bs4 import BeautifulSoup as bs
import requests
import csv


source = requests.get(
    "").text

soup = bs(source, "lxml")

csv_file = open("food_challenge_location.csv", "a", encoding="utf-8")
csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["Restaurant address", "Challenge name", "Location name"])

for food in soup.find_all(class_="chall-right"):
    wings = food.find("div", class_="result-address").text
    print(wings)

    burgers = food.find("div", class_="result-title").text
    print(burgers)

    fries = food.find("div", class_="result-where").text
    print(fries)

    csv_writer.writerow([wings, burgers, fries])

csv_file.close()
