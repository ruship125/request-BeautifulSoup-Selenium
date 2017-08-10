# Your can Use this script to scarp words from websites


import requests, bs4
exampleFile = requests.get('http://www.dabur.com/in/en-us/product')
exampleFile.raise_for_status()
exampleSoup = bs4.BeautifulSoup(exampleFile.text, 'lxml')
elems = exampleSoup.select('.cbp-l-grid-projects-title')
type(elems)


for prod in elems:
	print (prod.getText())
