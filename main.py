from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

bot = Chrome()
bot.get("https://lajumate.ro/")
bot.maximize_window()


cookie_button = bot.find_element(By.ID, "onetrust-accept-btn-handler")
cookie_button.click()

login_button = bot.find_element(By.ID, "login_action")
login_button.click()

email_field = bot.find_element(By.ID, "email")
email_field.send_keys("mihaiciorobitca985@gmail.com")

password_field = bot.find_element(By.ID, "password")
password_field.send_keys("Qwerty123.")

authenticate_button = bot.find_element(
    By.CSS_SELECTOR,
    "#login_form > input.buttons.btn_default_color.login_auth.rounded.shadow",
)
authenticate_button.click()

sleep(1)

new_url = "https://lajumate.ro/anunt/nou"
bot.get(new_url)

sleep(1)
title_field = bot.find_element(By.ID, "title")
title_field.send_keys("This is just a title")

sleep(0.5)
description_field = bot.find_element(By.ID, "description")
description_field.send_keys("Normal simple not complex description")

sleep(0.5)
price_field = bot.find_element(By.ID, "price")
price_field.send_keys("5000000000")

sleep(0.5)
euro_button = bot.find_element(By.CSS_SELECTOR, "#euro_holder > div > label")
euro_button.click()

sleep(0.5)
categorie_field = bot.find_element(By.ID, "category-field")
categorie_field.click()

sleep(0.2)
subfield_for_categorie = bot.find_element(By.ID, "categ_name_3")
subfield_for_categorie.click()

sleep(0.2)
subfield2_for_categorie = bot.find_element(By.ID, "categ_name_39")
subfield2_for_categorie.click()

sleep(0.2)
type_option = bot.find_element(By.ID, "type")
type_select = Select(type_option)
type_select.select_by_value("1")

sleep(0.2)
ticking_box = bot.find_element(By.ID, "terms")
bot.execute_script('document.getElementById("terms").click();', ticking_box)
#tick the box.

sleep(0.2)
input_element = bot.find_element(By.ID, "insert_new" )
input_element.click()
input()

