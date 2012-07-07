from requests import *

r = get('http://google.ca')
print r.url
# print r.text
print r.json
border_top_loc = r.text.index('border-top:')
semicolon = r.text.index(';',border_top_loc)
print r.text[border_top_loc:semicolon+1]