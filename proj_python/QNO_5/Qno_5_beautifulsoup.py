import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('https://techlekh.com/')	#send request to techlekh
list_links=[]												#initialize empty list

for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):	#select tag a only from soup
    if link.has_attr('href'):		# a attribute href
        #print(link['href'])
        list_links.append(link['href'])		#appending href content in the list

print(list_links)		
fp = open("link_store.txt", "w")		# writing the contents in the file line by line
for x in list_links:
    fp.write(x + '\n')
fp.close()
