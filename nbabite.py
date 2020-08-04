from selenium import webdriver, common
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(' — headless')
chrome_options.add_argument(' — no-sandbox')
chrome_options.add_argument(' — disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)


cc_streams_link1 = '//*[@id="content"]/div/div[5]/div[4]/div/ul[2]/li[1]/div/a'
cc_streams_link3 = '//*[@id="content"]/div/div[5]/div[4]/div/ul[2]/li[3]/div/a'
cc_list = '//*[@id="content"]/div/div[5]/div[4]/div/ul[2]'

cc_streams_link = '//*[@id="content"]/div/div[5]/div[4]/div/ul[2]/li[{}]/div/a'

driver.get("https://nbastreams.cc/")
sleep(3)
links = []
i = 1
while True:
    try:
        links.append(driver.find_element_by_xpath(cc_streams_link.format(i)).get_attribute('href'))
        i+=1
    except common.exceptions.NoSuchElementException:
        driver.quit()
        break
for link in links:
    print(link)