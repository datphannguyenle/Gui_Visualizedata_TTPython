from requests_html import HTMLSession
s = HTMLSession()
query = 'Hồ Chí Minh'
url = f'https://www.google.com/search?q=weather+{query}'
r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'})
#print(r.html.find('span#wob_tm', first=True).text)
#print(r.html.find('div.wNE31c', first=True).find('div.gNCp2e span.wob_t', first=True).text)
#print(r.html.find('div.wob_df.wob_ds', first=True).find('div.wNE31c', first=True).find('div.gNCp2e span.wob_t', first=True).text)
print(r.html.find('div.R3Y3ec.rr3bxd', first=True).find('div.wob_df.wob_ds'))