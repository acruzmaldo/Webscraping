'''
Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a 
formatted output one currency at a time. The output should display the name of the currency, the symbol 
(if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)

Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for 
BTC and $3,000 for ETH.
'''

import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = 'https://crypto.com/price'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

#table = soup.findAll('table')
currency_names = soup.findAll('span', attrs={'class': 'chakra-text css-1jj7b1a'}) 
price = soup.findAll('div', attrs={'class': 'css-b1ilzc'})
percent_change = soup.findAll('p',attrs={'class':'chakra-text css-z6ljr8', 'class':'chakra-text css-1okxd'})
table = soup.findAll('div' ,attrs={'class':'css-16q9pr7'})

table2 = soup.findAll('td' ,attrs={'role':'gridcell'})
count = 0
for i in percent_change:
    print(percent_change[count].text)
    count+=1

'''
count = 0
info = []
for i in table:
    info += table[count].text.split('+'or'-')
    #print(table[count].text)
    count += 1
print(len(info))

#currency_table = table[1]
#print(table)

'''

'''


count =0
for i in range(5):
    name = table2[count].text
    current_price = table2[count+1].text
    change = table2[count+5].text
    print(f'Name: {name}')
    print(f'Current Price: {current_price}')
    print(f'Percent Change: {change}')
    print()
    count += 9


    if name == 'BTC':
        current_price = price[count].text
        change = percent_change[count].text
        print(f'Name: {name}')
        print(f'Current Price: {current_price}')
        print(f'Percent Change: {change}')
        print()

    if name == 'ETH':
        current_price = price[count].text
        change = percent_change[count].text
        print(f'Name: {name}')
        print(f'Current Price: {current_price}')
        print(f'Percent Change: {change}')
        print(f'Opening Price: {float(change[:-1])}')
        print()
    '''
    


'''
message = "Chapter: " + str(num) + " Verse: " + my_verse
print(message)


import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

Twilionumber = '+16054154846'

myCellPhone = '+19364949192'

#send txt 
textmessage = client.messages.create(to=myCellPhone,from_=Twilionumber,
                body=message)

print(textmessage.status)
'''

'''
count = 0
name = soup.findAll('span')
for i in name:
    print(name[count].text)
    input()
    count += 1
'''