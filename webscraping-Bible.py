import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


num = random.randrange(1,22,1)

if num < 10:
    num = '0' + str(num)

url = 'https://ebible.org/asv/JHN' + str(num) + '.htm'

webpage = url


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')


page_verses = soup.findAll('div', class_ = 'main')

#print(page_verses)

for verse in page_verses:
    verse_list = verse.text.split('.')

# explore regex for more fine-tuned verse splitting

#print(verse_list)

my_verse = random.choice(verse_list[:-5])

print(f"Chapter: {num}, Verse:{my_verse}")

message = "Chapter:" + str(num) + " Verse:" + my_verse

import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

Twilionumber = '+16054154846'

myCellPhone = '+19364949192'

#send txt 
textmessage = client.messages.create(to=myCellPhone,from_=Twilionumber,
                body=message)

print(textmessage.status)

# task scheduler = can make my laptop run this code every day