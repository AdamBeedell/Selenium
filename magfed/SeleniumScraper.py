#SeleniumScraper.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

  

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.magfed.co.uk/all-events-and-walkons")

# Wait until events load, or insert a sleep if the page is JS-heavy
driver.implicitly_wait(5)

# Find the upcoming event section
events_section = driver.find_element(By.CLASS_NAME, "eventlist")

# Grab the first event article
first_event = events_section.find_element(By.CLASS_NAME, "eventlist-event")

# Extract the event link
event_link = first_event.find_element(By.CSS_SELECTOR, "a.eventlist-title-link").get_attribute("href")

# Extract the image URL (uses <img> tag)
img_url = first_event.find_element(By.TAG_NAME, "img").get_attribute("src")

# Extract the event title
event_title = first_event.find_element(By.CLASS_NAME, "eventlist-title").text



driver.get(event_link)


# --- DATE ---
date = driver.find_element(By.CLASS_NAME, "event-date").text

# --- TIME ---
time_start = driver.find_element(By.CLASS_NAME, "event-time-localized-start").text
time_end = driver.find_element(By.CLASS_NAME, "event-time-localized-end").text
event_time = f"{time_start} - {time_end}"

# --- BODY TEXT ---
body_container = driver.find_element(By.CLASS_NAME, "sqs-html-content")
paragraphs = body_container.find_elements(By.CLASS_NAME, "fadeIn")
body_text = "\n\n".join(p.text for p in paragraphs if p.text.strip())

# --- Print or store ---
print("Title:", event_title)
print("URL:", event_link)
#print("Image:", img_url)


print("Date:", date)
print("Time:", event_time)
print("Body:\n", body_text)

### send these values to zapier or whatever


