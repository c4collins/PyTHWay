# simple web scraper

from requests import * #gotta have my requests.
# I imported as * as the script only uses requests 

print "Welcome to the SimpleWebScraper!"
print "What page would you like to retrieve?"

site = raw_input("Please enter the address of the page you wish to scrape: ")
scrape_for = raw_input("What is the starting of the item you wish to search for: ")
end_at = raw_input("What is the ending of the item you wish to search for: ")

r = get(site)
item_start = r.text.index(scrape_for)
item_end = r.text.index(end_at,item_start)

print "\nRetrieving data from %s" % r.url
# print r.text
# print r.json

print "\nHere's what you're looking for:\n"
print r.text[item_start:item_end+len(end_at)]
print "\n"