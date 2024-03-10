from selenium.webdriver.common.by import By


class HeaderPageLocators:
    LOGO_SCOOTER = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    IMG_SCOOTER = By.XPATH, '//img[@src="/assets/scooter.png" and @alt="Scooter blueprint"]'
    LOGO_YANDEX = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'
    LOGO_DZEN = By.XPATH, '//svg[@class="desktop-base-header__logoBrand-3W desktop-base-header__isMorda-mX"]'
    BUTTON_CLOSE = By.XPATH, ('//span[@class="j8e989803 a379ed7a7 x1a8fe7df f71347ac1" and @tabindex="0"]/svg/g['
                              '@fill="inherit"]')
