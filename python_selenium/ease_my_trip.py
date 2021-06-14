import time

from selenium import webdriver

# Launching ChromeDriver
driver = webdriver.Chrome(
    executable_path="F:\\Users\\maila\\PycharmProjects\\python_testing\\driver\\chromedriver_win32\\chromedriver.exe")

# Navigation to website
driver.get("https://www.easemytrip.com/flights.html")
driver.maximize_window()
time.sleep(3)

# Clicking on Round-trip-radio-button
driver.find_element_by_xpath("//li[text()='Round-Trip']").click()

# Clicking on From
from_location = driver.find_element_by_id("FromSector_show")
from_location.click()

# Selecting Mumbai in "From" field
from_places = driver.find_elements_by_xpath("//ul/li/div/span[@class='ct']")

for place in from_places:
    if place.text == "Mumbai(BOM)":
        place.click()
        break

# Clicking on To
driver.find_element_by_id("Editbox13_show").click()

# Selecting Bangalore in "To" field
to_places = driver.find_elements_by_xpath("//ul/li/div/span[@class='ct']")
for place in to_places:
    if place.text == "Bangalore(BLR)":
        place.click()
        break

# Calendar (From) selection
driver.find_element_by_id("ddate").click()

from_months = driver.find_elements_by_xpath("//div[@class='month2']")

for month in from_months:
    if month.text == "JUL 2021":
        days = month.find_elements_by_xpath("./parent::div/parent::div //div[@class='days']/ul/li")
        for day in days:
            if day.text == "12":
                day.click()
                break

# Calendar (To) selection
driver.find_element_by_id("rdate").click()

month_dict = {"1": "Jan",
              "2": "Feb",
              "3": "Mar",
              "4": "Apr",
              "5": "May",
              "6": "Jun",
              "7": "Jul",
              "8": "Aug",
              "9": "Sep",
              "10": "Oct",
              "11": "Nov",
              "12": "Dec"}
year = "2021"
day = "24"

to_day = driver.find_element_by_xpath(
    f"//div[text()='{month_dict['8']} {year}']/parent::div/parent::div //div[@class='days']/ul/li[text()='{day}']")
to_day.click()

# driver.close()
