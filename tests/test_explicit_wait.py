from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import SOURCE


def test_check_title(browser):
    browser.get(SOURCE["main"])
    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.title_is("Your Store"))
    wait.until(EC.visibility_of_element_located((By.ID, "top")))
    wait.until(EC.presence_of_element_located(By.ID, "logo"))
    wait.until(EC.presence_of_element_located(By.ID, "search"))
    wait.until(EC.presence_of_element_located(By.ID, "cart"))
    wait.until(EC.presence_of_element_located(By.ID, "menu"))
    el = wait.until(EC.visibility_of_element_located((By.ID, "category")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "category"), "Categories"))
    assert el.text == "Categories"


def test_check_catalog(browser):
    browser.get(SOURCE["desktops"])
    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.title_is("Desktops"))
    wait.until(EC.visibility_of_element_located((By.ID, "top")))
    wait.until(EC.presence_of_element_located(By.ID, "logo"))
    wait.until(EC.presence_of_element_located(By.ID, "search"))
    wait.until(EC.presence_of_element_located(By.ID, "cart"))
    wait.until(EC.presence_of_element_located(By.ID, "menu"))
    el = wait.until(EC.visibility_of_element_located((By.ID, "category")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "category"), "Categories"))
    assert el.text == "Categories"


def test_check_product(browser):
    browser.get(SOURCE["mac"])
    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.title_is("iMac"))
    wait.until(EC.visibility_of_element_located((By.ID, "top")))
    wait.until(EC.presence_of_element_located(By.ID, "logo"))
    wait.until(EC.presence_of_element_located(By.ID, "search"))
    wait.until(EC.presence_of_element_located(By.ID, "cart"))
    wait.until(EC.presence_of_element_located(By.ID, "menu"))
    el = wait.until(EC.visibility_of_element_located((By.ID, "category")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "category"), "Categories"))
    assert el.text == "Categories"


def test_check_login_admin(browser):
    browser.get(SOURCE["admin"])
    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.title_is("Administration"))
    wait.until(EC.visibility_of_element_located((By.ID, "top")))
    wait.until(EC.presence_of_element_located(By.ID, "logo"))
    wait.until(EC.presence_of_element_located(By.ID, "search"))
    wait.until(EC.presence_of_element_located(By.ID, "cart"))
    wait.until(EC.presence_of_element_located(By.ID, "menu"))
    el = wait.until(EC.visibility_of_element_located((By.ID, "category")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "category"), "Categories"))
    assert el.text == "Categories"


def test_check_user_register(browser):
    browser.get(SOURCE["register"])
    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(EC.title_is("Register Account"))
    wait.until(EC.visibility_of_element_located((By.ID, "top")))
    wait.until(EC.presence_of_element_located(By.ID, "logo"))
    wait.until(EC.presence_of_element_located(By.ID, "search"))
    wait.until(EC.presence_of_element_located(By.ID, "cart"))
    wait.until(EC.presence_of_element_located(By.ID, "menu"))
    el = wait.until(EC.visibility_of_element_located((By.ID, "category")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "category"), "Categories"))
    assert el.text == "Categories"
