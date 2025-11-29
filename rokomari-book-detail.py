from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# PROXY = "51.158.105.94:31826"

# Set up headless Chrome browser
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
# options = Options().add_argument(f'--proxy-server=https://{PROXY}')

driver = webdriver.Chrome(options=options)

# Target URL
url = 'https://www.rokomari.com/book/178414/paradoxical-sajid-2'
driver.get(url)
driver.maximize_window()

# Give time to load the page
time.sleep(3)

# Extract book name
book_name = driver.find_element(By.XPATH, '//*[@id="ts--desktop-details-book-main-info"]/div[1]/h1').text

# Extract price
price = driver.find_element(By.XPATH, '//*[@id="ts--desktop-details-book-main-info"]/div[6]/span[1]').text

# rating = driver.find_element(By.XPATH, '#rokomariBody > div.container > div:nth-child(6) > div:nth-child(1) > div > div.detailsReviewHeader_ratingContainer__RsQEw > div > div.detailsReviewHeader_ratingSummary___aFy_ > h3').text

summary = driver.find_element(By.XPATH, '//*[@id="ts--desktop-details-book-main-info"]/div[5]/div').text

print("Book Name:", book_name)
print("Price:", price)
# print("Rating:", rating)
print("Summary:", summary)

driver.quit()
