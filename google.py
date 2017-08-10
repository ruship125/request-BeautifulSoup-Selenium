import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

# Type Following code in command- line
# >> lucky Beautiful Soup
# Beautiful Soup is a search term 
# This program will open five different top 5 results of googles in five different tabs of browser