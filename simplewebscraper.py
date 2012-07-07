# simple web scraper

from requests import * #gotta have my requests.
# I imported as * as the script only uses requests 

print "\nWelcome to the SimpleWebScraper!"
print "Answer the following questions and you'll be given the first match from the page."
print """
An an example, try entering 
\t 'http://www.google.ca', 
\t 'border-top', and 
\t ';' 
as the answers to the following questions.
"""

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
print "\t", r.text[item_start:item_end+len(end_at)]
print