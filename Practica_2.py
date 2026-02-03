import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
positions=[]


driver = webdriver.Chrome()
driver.get("https://amberstudio.com/location-guadalajara")
wait = WebDriverWait(driver, 10)

def verifylink(currentlink):
    driver.switch_to.window(driver.window_handles[-1])
    if currentlink != driver.current_url:
        raise Exception("Wrong Link")
    else:
        print("Correct Link")

def amberstudio():
    driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
    driver.find_element(By.CSS_SELECTOR, "li.menu-item-has-children[data-v-6ccee347]").click()
    try:
        verifylink("https://jobs.jobvite.com/amberstudiocareers/")
    except Exception as e:
        print(e)

    locations = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[contains(@class, 'jv-button') and contains(@class, 'jv-button--hollow')]")
        )
    )

    print(len(locations))

    for location in locations:
        print(location.text)
        if location.text == "Guadalajara Careers":
            driver.execute_script("arguments[0].click();", location)
            break

def guadalajaracareers():
    try:
        verifylink("https://jobs.jobvite.com/amberstudiocareers/search?l=Guadalajara")
    except Exception as e:
        print(e)

def seniorcareers():
    driver.find_element(By.ID, "jv-list-search").send_keys("Senior" + Keys.ENTER)

    openings = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "a.jv-button.jv-button--hollow.flex-row.flex-m-space-between.flex-c-center")
        )
    )
    print(len(openings))

    for opening in openings:
        positions.append(opening.get_attribute("href"))
    print(positions)

amberstudio()
guadalajaracareers()
seniorcareers()

time.sleep(5)