from urllib.request import urlopen
page = urlopen('http://www.google.com')
s = page.read().decode()
