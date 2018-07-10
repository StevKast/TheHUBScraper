import requests, bs4, getpass, time
from selenium import webdriver
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class Scraper:

    def credpromt():
        user_login = input('Username: ')
        user_password = getpass.getpass('Password: ')

    def scrape(self, username, password):

        if False:
            credpromt()

        browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
        browser.get('https://muidp.miamioh.edu/cas/login')

        #time.sleep(3)
        #print(browser.find_element_by_id('username'))

        #print('Now on login page')
        try:
            print('Login attempt')
            loginField = browser.find_element_by_css_selector('#username')
            loginField.send_keys(username)
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
#End Scraper class

#########################
#  UI
#########################

# def LoginScreen():
#
#     #super(LoginScreen, self).__init__(**kwargs)
#     layout = BoxLayout(orientation='vertical', padding=('50','50'))
#     userLayout = BoxLayout(orientation='horizontal')
#     userLayout.add_widget(Label(text='User Name'))
#     username = TextInput(multiline=False)
#     userLayout.add_widget(username)
#     layout.add_widget(userLayout)
#     passLayout = BoxLayout(orientation='horizontal')
#     passLayout.add_widget(Label(text='Password'))
#     password = TextInput(password=True, multiline=False)
#     passLayout.add_widget(password)
#     layout.add_widget(passLayout)
    # return layout

class LoginForm(BoxLayout):

    login_cred = ObjectProperty()

    def get_login_cred(self, username, password):
        print('Unique Id: ' + username + " Password: " + password)
        user_login = username
        user_password = password
        Scraper().scrape(user_login, user_password)

class ScrapeApp(App):
    pass

#End MyApp class

if __name__ == '__main__':
    ScrapeApp().run()
