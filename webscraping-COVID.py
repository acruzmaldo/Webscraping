# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll('tr')

# get an entire row
'''
for row in table_rows[2:52]:
    print(row)
    input()
'''

# get element in row
count = 1

state_worst_death = ''
state_best_death = ''
high_death_rate = 0.0
low_death_rate = 100.0

state_worst_test = ''
state_best_test = ''
high_test_rate = 0.0
low_test_rate = 100.0

for row in table_rows[2:52]:
    td = row.findAll('td')

    state = td[count].text
    total_cases = int(td[count + 1].text.replace(',',''))
    total_deaths = int(td[count + 3].text.replace(',',''))
    total_tests = int(td[count + 9].text.replace(',',''))
    population = int(td[count + 11].text.replace(',',''))

    death_rate = round((total_deaths/total_cases) * 100, 2)
    test_rate = round((total_tests/population) * 100, 2)

    if death_rate > high_death_rate:
        high_death_rate = death_rate
        state_worst_death = state

    if death_rate < low_death_rate:
        low_death_rate = death_rate
        state_best_death = state


    if test_rate > high_test_rate:
        high_test_rate = test_rate
        state_worst_test = state

    if test_rate < low_test_rate:
        low_test_rate = test_rate
        state_best_test = state


    #print(state)
    #print(f"Cases: {total_cases}")
    #print(f"Deaths: {total_deaths}")
    #print(f"Tests: {total_tests}")
    #print(f"Population: {population}")
    #print(f"Death Rate: {death_rate}")
    #print(f"Test Rate: {test_rate}")
    #print('\n')    

print(f"State with the worst death rate: {state_worst_death}")
print(f"Death rate: {high_death_rate}% \n")
print(f"State with the best death rate: {state_best_death}")
print(f"Death rate: {low_death_rate}% \n\n")

print(f"State with the worst test rate: {state_worst_test}")
print(f"Test rate: {high_test_rate}% \n")
print(f"State with the best test rate: {state_best_test}")
print(f"Test rate: {low_test_rate}% \n\n")



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

