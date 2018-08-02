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
    print('logging in')
    driver.get("http://127.0.0.1:5000/login")
    #driver.save_screenshot('login_page.png')
    print('entering username!')
    driver.find_element_by_id("username").send_keys("admin")
    print('entering password')
    driver.find_element_by_id("password").send_keys("C@ntg3tme!n2018")
    print('submitting')
    driver.find_element_by_id("submit").click()
    print('im in... now going to read our fans messages')
    #driver.save_screenshot('on_dashboard.png')
    driver.get("http://127.0.0.1:5000/unread_messages")
    print('done reading')
    #driver.save_screenshot('reading_messages.png')
    print('logging out')
    driver.get("http://127.0.0.1:5000/logout")
    print('done')
    #driver.save_screenshot('going_baccdk_to_login.png')
    driver.quit()

bot_run()
