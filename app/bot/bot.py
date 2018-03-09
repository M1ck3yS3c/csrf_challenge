from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def bot_run():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
    )
    driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs", desired_capabilities=dcap)
    driver.set_window_size(1120, 550)
    print('anything')
    driver.get("http://0.0.0.0:8000/login")
    driver.save_screenshot('login_page.png')
    print('anything1')
    driver.find_element_by_id("username").send_keys("mholloway")
    print('anything2')
    driver.find_element_by_id("password").send_keys("C@ntg3tme!n")
    print('anything3')
    driver.find_element_by_id("submit").click()
    print('anything4')
    driver.save_screenshot('on_dashboard.png')
    driver.get("http://0.0.0.0:8000/unread_messages")
    print('anything5')
    driver.save_screenshot('reading_messages.png')
    print('anything6')
    driver.get("http://0.0.0.0:8000/logout")
    driver.save_screenshot('going_baccdk_to_login.png')
    driver.quit()

bot_run()
