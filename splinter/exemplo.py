from splinter import Browser

browser = Browser()
browser.visit('http://localhost:8000/admin/')
browser.fill('username', 'andrews')
browser.fill('password', 'andrews')
browser.find_by_css('input[type="submit"]').click()
browser.is_text_present('Site administration')
browser.quit()
