#\31 303889_231f30be-afa7-406f-babf-a50d00af8f8d > div:nth-child(3)

#\31 303889_231f30be-afa7-406f-babf-a50d00af8f8d > div:nth-child(3)

#\34 88841_4653d42a-d11c-4707-a8dc-a657014aaba2 > div:nth-child(3)

#react-app > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > h1

import requests, bs4, getpass, time
from selenium import webdriver

# res = requests.get('https://muhub.campuslabs.com/engage/organization/kode2learn')
# print(res.raise_for_status)
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# name = soup.select('#react-app > div > div:nth-of-type(2) > div > div > div:nth-of-type(4) > div > div > div > div:nth-of-type(1) > span:nth-of-type(1) > h2')
#
# print(len(name))
# print(name)
#
# res = requests.get('http://thetataumiami.com/members')
# print(res.raise_for_status)
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# name = soup.select('body > div.container-fluid > div > div:nth-of-type(1) > h3')
#
# print(len(name))
# print(name)


login = input('Username: ')
password = getpass.getpass('Password: ')

browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
#time.sleep(3)
browser.get('https://muidp.miamioh.edu/cas/login')

#time.sleep(3)
#print(browser.find_element_by_id('username'))

print('Now on login page')
try:
    print('Login attempt')
    loginField = browser.find_element_by_css_selector('#username')
    loginField.send_keys(login)
    print('Found loginField')
    passField = browser.find_element_by_css_selector('#password')
    passField.send_keys(password)
    passField.submit()
    print('Found passField')
except:
    print('Login not found')

time.sleep(3)

browser.get('https://muhub.campuslabs.com/engage/organization/kode2learn')
#Proceed to login if needed
try:
    signInButton = browser.find_element_by_css_selector('#react-app > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > a > div > span')
    print('Signing In')
    time.sleep(3)
    signInButton.click()
    time.sleep(3)
    print('Authenticated')
    time.sleep(5)
    primaryContact = browser.find_element_by_css_selector('#react-app > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(2) > div:nth-child(2)')
    print(primaryContact.text)
    elem = browser.find_element_by_css_selector('#\31 303889_231f30be-afa7-406f-babf-a50d00af8f8d')
    print(elem.text)
    elem.click()
    time.wait(1.5)
    name = browser.find_element_by_css_selector('#member_card_231f30be-afa7-406f-babf-a50d00af8f8d > div:nth-child(2) > div > div:nth-child(3)')
    print(name.text)
    email = browser.find_element_by_css_selector('#member_card_231f30be-afa7-406f-babf-a50d00af8f8d > div:nth-child(2) > div > div:nth-child(4) > a')
    print(email.text)
except:
    print('Not found!')

#<div id="1303889_231f30be-afa7-406f-babf-a50d00af8f8d" style="color: rgba(0, 0, 0, 0.87); background-color: rgb(255, 255, 255); transition: all 450ms cubic-bezier(0.23, 1, 0.32, 1) 0ms; box-sizing: border-box; font-family: &quot;Source Sans Pro&quot;, sans-serif; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 6px, rgba(0, 0, 0, 0.12) 0px 1px 4px; border-radius: 2px; margin: 10px 5px; padding: 20px 10px 5px; text-align: center; min-height: 200px;"><div #style="line-height: 0; margin-bottom: 20px;"><div alt="" size="75" style="color: rgb(255, 255, 255); background-color: rgb(101, 101, 101); user-select: none; display: inline-flex; align-items: center; justify-content: center; font-size: 37.5px; border-radius: 50%; height: 75px; width: 75px;">M</div></div><div style="font-size: 14px; text-overflow: ellipsis; overflow: hidden; font-weight: bold;">PRESIDENT</div><div style="margin: 5px 0px; font-size: 17px;">Mike Wedzikowski</div></div>

#time.sleep(3)
#TODO: Prompt login then open the hub to get data
time.sleep(10)
browser.quit()
