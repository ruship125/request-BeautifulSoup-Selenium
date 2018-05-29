import requests
import bs4
import time

def spider(max_pages):
	page = 1
	while page < max_pages:
		url = "https://www.justdial.com/Thane/Sweet-Shops-in-Thane/nct-10465567/page-%s" % page
		crawl_url = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		crawl_url.raise_for_status()
		soup = bs4.BeautifulSoup(crawl_url.text, 'lxml')
		for elems in soup.find_all('span', class_="jcn"):
			select_a = elems.select('a')
			for links in select_a:
				href = links.get('href')
				time.sleep(1)
				res = requests.get(href, headers={'User-Agent': 'Mozilla/5.0'})
				xsoup = bs4.BeautifulSoup(res.text, 'lxml')
				Name = xsoup.select('.fn')
				tel = xsoup.select('.tel')
				add = xsoup.select('.adrstxtr')
				a = Name[0]
				atext = a.getText()
				print("<p>%s</p>" % atext)
				print("--"*10)
				try :
					b = tel[0]
					btext = b.getText()
					print("<il>%s</il>" % btext)
				except IndexError:
					print("<il>No Number</il>")
				print("--"*10)
				c = add[0]
				ctext = c.getText()
				print("<ol>%s</ol>" % ctext)
				print("=="*25)
		page += 1
		time.sleep(2)


spider(41)

