from splinter import Browser


USER_NAME = 'dasenok@gmail.com'
USER_PASSWORD = '12345nov'
PROFILE_URL = 'https://testingbot.com/members'

browser = Browser('chrome')
browser.visit('https://testingbot.com/')
print "--Login test--"
print "click 'Sign In' button"
browser.find_by_xpath("//ul[contains(@class, 'right')]//a[@href='users/sign_in']").click()
print 'enter user name'
browser.find_by_id('user_email').type(USER_NAME)
print 'enter user password'
browser.find_by_id('user_password').type(USER_PASSWORD)
print "click 'Submit'"
browser.find_by_name('commit').click()
print "Expected " + PROFILE_URL
assert browser.driver.current_url == PROFILE_URL
print 'PASSED'
browser.quit()
	