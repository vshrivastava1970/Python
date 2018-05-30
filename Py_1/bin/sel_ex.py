
from selenium import webdriver

b = webdriver.Chrome()
b.get('http://www.google.com')

assert 'Google' in b.title
print('open successful')
field = b.find_element_by_id('lst-ib')
field.send_keys('Python')
from selenium.webdriver.common.keys import Keys
field.send_keys(Keys.RETURN)