import requests, bs4, getpass, time
from selenium import webdriver

login = input('Username: ')
password = getpass.getpass('Password: ')

browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
browser.get('https://muidp.miamioh.edu/cas/login')

#time.sleep(3)
#print(browser.find_element_by_id('username'))

#print('Now on login page')
try:
    print('Login attempt')
    loginField = browser.find_element_by_css_selector('#username')
    loginField.send_keys(login)
    #print('Found loginField')
    passField = browser.find_element_by_css_selector('#password')
    passField.send_keys(password)
    passField.submit()
    #print('Found passField')
except:
    print('Login not found')

time.sleep(1)

browser.get('https://muhub.campuslabs.com/engage/organizations')
#Proceed to login if needed

signInButton = browser.find_element_by_css_selector('#react-app > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > a > div > span')
print('Signing In')
time.sleep(1)
signInButton.click()
time.sleep(1)
print('Authenticated')
time.sleep(1)

#Find org on page
item = 1;
while item < 754:

    time.sleep(1)

    org = browser.find_element_by_css_selector('#org-search-results > div > div > div:nth-child(' + str(item) + ')')
    org.click()

    time.sleep(2)

    try:
        orgName = browser.find_element_by_css_selector('#react-app > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > h1')
        print('Org Name: ' + orgName.text)
        primaryContact = browser.find_element_by_css_selector('#react-app > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(2) > div:nth-child(2)')
        print("Primary Contact: " + primaryContact.text)
        pass
    except:
        print('No Contact Info')

    time.sleep(2)

    browser.back()

    if item % 10 == 0:
        loadMore = browser.find_element_by_css_selector('#react-app > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > button > div > div > span')
        loadMore.click()

    item += 1

#TODO: Export to CSV
time.sleep(10)
browser.quit()
