from selenium import webdriver


def bot_run():
    print('in bot!')
    print('in run bot!')
    driver = webdriver.PhantomJS(executable_path="phantomjs")
    driver.set_window_size(1120, 550)
    print('anything')
    driver.get("http://127.0.0.1:5000/login")
    driver.save_screenshot('screenshot2.png')
    print('anything1')
    driver.find_element_by_id("username").send_keys("mholloway")
    print('anything2')
    driver.find_element_by_id("password").send_keys("C@ntg3tme!n")
    print('anything3')
    driver.find_element_by_id("submit").click()
    print('anything4')
    driver.get("http://127.0.0.1:5000/unread_messages")
    print('anything5')
    driver.save_screenshot('screenshot1.png')
    print('anything6')
    driver.quit()

