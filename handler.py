from time import sleep
from selenium import webdriver, common
from selenium.webdriver.chrome.options import Options


def lambda_handler(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)
    driver.get("https://nbastreams.cc/")
    body = f"Headless Chrome Initialized, Page title: {driver.title}"
    sleep(3)
    links = []
    i = 1
    cc_streams_link = '//*[@id="content"]/div/div[5]/div[4]/div/ul[2]/li[{}]/div/a'
    while True:
        try:
            links.append(driver.find_element_by_xpath(cc_streams_link.format(i)).get_attribute('href'))
            i += 1
        except common.exceptions.NoSuchElementException:
            driver.quit()
            break
    for link in links:
        print(link)
    driver.close();
    driver.quit();
    return {
        "statusCode": 200,
        "body": body
    }
#

if __name__ == "__main__":
    x = lambda_handler({}, {})
    print(x)