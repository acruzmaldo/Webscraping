'''
Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a 
formatted output one currency at a time. The output should display the name of the currency, the symbol 
(if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)

Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for 
BTC and $3,000 for ETH.
'''

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://crypto.com/price'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')



print('Top 5 Cryptos')
print()

tablecells = soup.findAll('td' ,attrs={'role':'gridcell'})
currency_names = soup.findAll('p', attrs={'class': 'chakra-text css-rkws3'})
ticker = soup.findAll('span', attrs={'class': 'chakra-text css-1jj7b1a'}) 
price = soup.findAll('div', attrs={'class': 'css-b1ilzc'})


# while loop method of finding top 5
change = 4
count = 0

while count < 5:
    price_mod = round(float(price[count].text[1:].replace(',','')),2)
    #print(price_mod)
    opening_price = format(price_mod - (price_mod * (float(tablecells[change].text.strip('%'))/100)),',.2f')
    print(f'{count + 1}) Name: {currency_names[count].text} - {ticker[count].text} || Price: ${format(price_mod,",.2f")} || Percent Change: {tablecells[change].text} || Opening Price: ${opening_price}')
    #print(float(tablecells[change].text.strip('%')))
    print()
    change += 9
    count += 1

import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

Twilionumber = '+16054154846'

myCellPhone = '+19364949192'

count = 0
for i in currency_names: 
    
    name = ticker[count].text
    price_mod = round(float(price[count].text[1:].replace(',','')),2)

    if name == 'BTC' and price_mod <= 40000.00:
        message = "Bitcoin is below $40,000 hurry up and BUY BUY BUY!!!"
        #send txt 
        textmessage = client.messages.create(to=myCellPhone,from_=Twilionumber,
                body=message)
        print(message)
        print(textmessage.status)
        

    if name == 'ETH' and price_mod <= 3000:
        message = "Ethereum is below $3,000 hurry up and BUY BUY BUY!!!"
        #send txt 
        textmessage = client.messages.create(to=myCellPhone,from_=Twilionumber,
                body=message)
        print('\n'+message)
        print(textmessage.status)
    
    count += 1





