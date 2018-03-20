#OverPy by Sam
#Stats scraper for Overwatch

import requests
import lxml
from lxml import etree

class Player:

    def __init__(self, region, platform, username):
        self.region = region
        self.platform = platform
        self.username = username
        self.url = "https://playoverwatch.com/{}/career/{}/{}".format(self.region, self.platform, self.username)

    def get_stats(self):
        stats = {}
        hero_id = {'0x02E00000FFFFFFFF':'ALL HEROES',
                        '0x02E0000000000002':'REAPER',
                        '0x02E0000000000003':'TRACER',
                        '0x02E0000000000004':'MERCY',
                        '0x02E0000000000006':'TORBJORN',
                        '0x02E0000000000007':'REINHARDT',
                        '0x02E0000000000008':'PHARAH',
                        '0x02E0000000000009':'WINSTON',
                        '0x02E000000000000A':'WIDOWMAKER',
                        '0x02E0000000000015':'BASTION',
                        '0x02E0000000000016':'SYMMETRA',
                        '0x02E0000000000020':'ZENYATTA',
                        '0x02E0000000000040':'ROADHOG',
                        '0x02E0000000000042':'MCCREE',
                        '0x02E0000000000065':'JUNKRAT',
                        '0x02E0000000000068':'ZARYA',
                        '0x02E000000000006E':'SOLDIER: 76',
                        '0x02E0000000000079':'LUCIO',
                        '0x02E000000000007A':'D.VA',
                        '0x02E000000000013B':'ANA',
                        '0x02E000000000013E':'ORISA',
                        '0x02E00000000001A2':'MOIRA',
                        'TO BE DETERMINED':'BRIGITTE'}



        page = requests.get(self.url)
        parsed_page = etree.HTML(page.text)
        x = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div""") #how many heroes to parse?
        heroes_to_parse = len(x) - 1 #subtracting 1 because first item in xpath is not a hero

        for heroes in range(heroes_to_parse):
            y = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div[{}]/div""".format(str(heroes + 2))) #adding 2 because range starts at 0 and first hero starts at 2
            categories_to_parse = len(y)
            hero_num = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div[{}]""".format(str(heroes + 2)))[0].attrib.get('data-category-id')
            hero = hero_id[hero_num]
            stats[hero] = {}

            for categories in range(categories_to_parse):
                z = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div[{}]/div[{}]/div/table/tbody/tr""".format(str(heroes + 2), str(categories + 1)))
                items_to_parse = len(z)

                for items in range(items_to_parse):
                    a = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div[{}]/div[{}]/div/table/tbody/tr[{}]/td[1]""".format(str(heroes + 2), str(categories + 1), str(items + 1)))
                    b = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div[{}]/div[{}]/div/table/tbody/tr[{}]/td[2]""".format(str(heroes + 2), str(categories + 1), str(items + 1)))
                    stats[hero][a[0].text.upper()] = b[0].text.upper()

        return stats
