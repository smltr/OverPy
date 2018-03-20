from selenium import webdriver

#OverPy by Sam
#Project to scrape player stats from playoverwatch.com

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

class Overpy_Player:

    def __init__(self, region, platform, username):
        #region e.g. 'en-us'
        #username e.g. 'Player-1234' --case sensitive!--
        #platform e.g. 'pc' 'psn' 'xbl'
        self.region = region
        self.platform = platform
        self.username = username
        self.url = "https://playoverwatch.com/{}/career/{}/{}".format(self.region, self.platform, self.username)

    def get_all_heros(self):
        driver.get(self.url)
        driver.find_element_by_xpath("""//*[@id="profile-btn-switcher"]/a[2]""").click()
        elements_text = []
        elements = driver.find_elements_by_class_name('stat-title')
        for i in elements:
            if i.text != '':
                elements_text.append(i.text)

        stats = {}
        for i in elements_text:
            elems = driver.find_elements_by_xpath("""//*[@id="competitive"]/section[3]/div/div[2]/div[{}]/div/table/tbody/tr""".format(str(elements_text.index(i) + 1)))
            for x in range(len(elems)):
                a = driver.find_element_by_xpath("""//*[@id="competitive"]/section[3]/div/div[2]/div[{}]/div/table/tbody/tr[{}]/td[1]""".format(str(elements_text.index(i) + 1), str(x + 1)))
                b = driver.find_element_by_xpath("""//*[@id="competitive"]/section[3]/div/div[2]/div[{}]/div/table/tbody/tr[{}]/td[2]""".format(str(elements_text.index(i) + 1), str(x + 1)))
                stats[a.text] = b.text

        return stats

Cyrk = Overpy_Player('en-us', 'pc', 'Cyrk-1234')
print(Cyrk.get_all_heros())

#//*[@id="competitive"]/section[3]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[1]
#//*[@id="competitive"]/section[3]/div/div[2]/div[4]/div/table/thead/tr/th/h5
#//*[@id="competitive"]/section[3]/div/div[2]/div[3]/div/table/thead/tr/th/h5
#//*[@id="competitive"]/section[3]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[1]
#//*[@id="competitive"]/section[3]/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]
#//*[@id="competitive"]/section[3]/div/div[2]/div[1]/div/table/tbody/tr[2]/td[2]
#BARRIER DAMAGE DONE
#//*[@id="competitive"]/section[3]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[1]
#194,722
#//*[@id="competitive"]/section[3]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]
#MELEE FINAL BLOWS
#//*[@id="competitive"]/section[3]/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]
