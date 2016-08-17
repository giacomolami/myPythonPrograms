import urllib2, urllib
import re
import sys
# url ='http://www.yahoo.com'
#connect to a URL
url = 'http://' + str(sys.argv[1])
print(url)
website = urllib2.urlopen(url)

#read html code
html = website.readlines()
print(len(html))

#use re.findall to get all the links
links = []
i = 0
while (len(links) == 0):  
   links = re.findall('"((http|ftp)s?://.*?)"', html[i])
   i = i+1

if (len(links)>0):
  print 'Found the first LINK at line number ', i
print links

urllib.urlretrieve(url, filename="content")
exit()

