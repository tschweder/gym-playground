import scrapy
import time
import re
import json


class CryptoSpider(scrapy.Spider):
    name = 'crypto'

    def start_requests(self):
        yield scrapy.Request(url='https://coinmarketcap.com/historical/20130428/', callback=self.parse)

    def parse(self, response):
        time.sleep(10)  # so server is not killing the crawler
        table_rows = response.css('tr.cmc-table-row').getall()
        i = 0
        coins_json = []
        for table_row in table_rows:
            # because the website is loading dynamically (and I don't need more) we keep it at the top 20 coins
            if i >= 20:
                break
            # print('---------------------------------------')
            price = '0'
            name = 'Error'
            supply = '0'
            string_row = ''.join(table_row)
            string_row_list = re.split(r'<|>', string_row)
            for index, element in enumerate(string_row_list):
                # print("%d :" % index + element)
                if 'cmc-table__cell--sort-by__circulating-supply' in element:
                    supply = string_row_list[index + 3]
                elif 'cmc-table__cell--sort-by__price' in element:
                    price = string_row_list[index + 3]
                elif 'class="cmc-table__column-name--name cmc-link"' in element:
                    name = string_row_list[index + 1]
            coin = {'name': name,
                    'price': price,
                    'supply': supply}
            coins_json.append(json.dumps(coin, indent=3))
            i += 1

        url_date = response.url.split('/')[-2]
        filename = f'data\\crypto-data-from-{url_date}.json'
        with open(filename, 'w') as f:
            json.dump(coins_json, f)
            # for coin_json in coins_json:
            #     json.dump(coin_json, f)

        # gets all links from the div that contains the next week button
        links = response.css('a.iv7acg-0.iqSSDO.cmc-link::attr(href)').getall() 
        
        # used to determine which is the next and not the previous button 
        date = 0
        
        # goes through all links in the div and finds out which is the correct one
        for link in links:
            date_link = link.split('/')[2]
            if date_link is not '':
                if date < int(date_link):
                    date = int(date_link)
                    next_link = link
                    
        # catches the last page where there is no next week            
        if date != 0:
            # set the next week as new request and calls parse() again
            next_page = response.urljoin(next_link)
            yield scrapy.Request(next_page, callback=self.parse)
