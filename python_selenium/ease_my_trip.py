import time

from selenium import webdriver

# Launching ChromeDriver
driver = webdriver.Chrome(
    executable_path="F:\\Users\\maila\\PycharmProjects\\python_testing\\driver\\chromedriver_win32\\chromedriver.exe")

# Navigation to website
driver.implicitly_wait(8)
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
    if place.text == "Kolkata(CCU)":
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

# Click on dropdown menu to select passenger
driver.find_element_by_css_selector(".dropbtn_n").click()
time.sleep(2)

# Selecting one more adult
driver.find_element_by_xpath("//input[@class='plus_box1']").click()

# selecting 2 children
for i in range(1, 3):
    driver.find_element_by_xpath("//input[@class='plus_boxChd']").click()

# Selecting business class radio button
business_class_value = "3"
driver.find_element_by_xpath(f"//div[@id='myDropdown_n']/div/label[{business_class_value}]").click()
time.sleep(2)

# Click on Done button
driver.find_element_by_css_selector(".dn_btn").click()

# Click on search button
driver.find_element_by_css_selector(".src_btn").click()
time.sleep(10)

# Take screenshot
driver.get_screenshot_as_file("booking_page.png")

# Click on Book Now
driver.find_element_by_css_selector("#BtnBookNow").click()

# Click on Continue
driver.find_element_by_xpath("//a[text()='Continue']").click()
time.sleep(2)

# Scrolling page down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# do not insure trip
driver.find_element_by_xpath("//div[@class='insur-no']/label/input[@name='rdoInsuNew']").click()

checkbox = driver.find_element_by_xpath("//label[@for='chkPubReliefFund']")
checkbox_tick = checkbox.click()

if not checkbox_tick:
    checkbox_status = checkbox.is_selected()
    assert checkbox_status == False
else:
    checkbox.click()

# Enter email
driver.find_element_by_id("txtEmailId").send_keys("aritrasur47@example.com")

# Click on Continue Booking
driver.find_element_by_xpath("//span[text()='Continue Booking']").click()
time.sleep(2)

driver.close()
