from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT = (By.XPATH, './/p[text()="Личный Кабинет"]') # Кнопка Личный Кабинет
    REGISTRATION = (By.XPATH, './/button[text()="Зарегистрироваться"]') # Кнопка Зарегистироваться
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле ввода email
    PASSWORD_INPUT = (By.NAME,"Пароль") # Поле ввода пароля
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Поле ввода Имени
    LOGIN_BUTTON = (By.XPATH,'.//button[text()="Войти"]') # Кнопка Войти
    ERROR_TEXT = (By.XPATH,'.//p[text()="Некорректный пароль"]') # Текст Некорректный пароль
    SING_IN_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0') # Кнопка Войти в аккаунт
    PLACE_AN_ORDER_BUTTON = (By.CLASS_NAME,'button_button__33qZ0') # Кнопка оформить заказ
    CONSTRUCTOR_BUTTON = (By.XPATH,'.//p[text()="Конструктор"]') # Кнопка Конструктор
    SING_IN_BUTTON_REGFORM = (By.CLASS_NAME, 'Auth_link__1fOlj') # Кнопка Войти на форме регистрации
    LOGOUT_BUTTON = (By.CLASS_NAME,'Account_button__14Yp3') # Кнопка Выход\
    LOGO_BUTTON = (By.CLASS_NAME,'AppHeader_header__logo__2D0X2') # Логотип
    BUNS_BUTTON = (By.XPATH,"//span[text()='Булки']") # Кнопка Булки
    SAUCES_BUTTON = (By.XPATH,"//span[text()='Соусы']") # Кнопка Соусы
    FILLINGS_BUTTON = (By.XPATH,"//span[text()='Начинки']") # Кнопка Начинки
    BUNS_TAB_ACTIVE = (By.XPATH,"//div[contains(@class,'tab_type_current')]//span[text()='Булки']") # Активная кнопка булки
    SAUCES_TAB_ACTIVE = (By.XPATH,"//div[contains(@class,'tab_type_current')]//span[text()='Соусы']") # Активная кнопка соусы
    FILLINGS_TAB_ACTIVE = (By.XPATH,"//div[contains(@class,'tab_type_current')]//span[text()='Начинки']") # Активная кнопка начинки