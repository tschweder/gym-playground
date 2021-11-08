import scrapy
import time
import re
from gym.utils.crypto_coin import CryptoCoin


class CryptoSpider(scrapy.Spider):
    name = 'crypto'

    def start_requests(self):
        yield scrapy.Request(url='https://coinmarketcap.com/historical/20130428/', callback=self.parse)

    def parse(self, response):
        time.sleep(10)  # so server is not killing the crawler
        table_rows = response.css('tr.cmc-table-row').getall()
        url_date = response.url.split('/')[-2]
        filename = f'data\\crypto-data-from-{url_date}'
        with open(filename, 'wb') as f:
            i = 0
            for table_row in table_rows:
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
                        supply = string_row_list[index+3]
                    elif 'cmc-table__cell--sort-by__price' in element:
                        price = string_row_list[index+3]
                    elif 'class="cmc-table__column-name--name cmc-link"' in element:
                        name = string_row_list[index+1]
                f.write(b"Name: ")
                f.write(bytes(name, 'utf-8'))
                f.write(b"\nPrice: ")
                f.write(bytes(price, 'utf-8'))
                f.write(b"\nSupply: ")
                f.write(bytes(supply, 'utf-8'))
                f.write(b"\n--------------------------------------------------\n")

                i += 1

        # i = 0
        # for element in string_row_list:
        #     print(element + " %d" % i)
        #     i += 1
                
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

