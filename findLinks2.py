import urllib, htmllib, formatter
import sys

url = 'http://' + str(sys.argv[1])
print(url)
website = urllib.urlopen(url)
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
for link in ptext.anchorlist:
  print(link) 
