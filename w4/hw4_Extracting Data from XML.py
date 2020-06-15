import urllib
#fhand=urllib.urlopen('http://python-data.dr-chuck.net/comments_42.xml')
fhand=urllib.urlopen('http://python-data.dr-chuck.net/comments_367934.xml')

import xml.etree.ElementTree as ET
tree = ET.fromstring(fhand.read())
counts = tree.findall('.//count')
print sum([int(count.text) for count in counts])

# my one:
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as BS
import ssl
import xml.etree.ElementTree as ET

# ignore ssl certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml' #sample
# url = 'http://py4e-data.dr-chuck.net/comments_460764.xml' #actual
html = urllib.request.urlopen(url, context=ctx).read()
soup = BS(html, 'html.parser')

print('Retrieving', url)

# counting characters
html = len(html)
print('Retrieved', html, 'characters')

count = 0
total = 0

# retrieving the numbers from the xml
tags = soup('count')
for tag in tags:
    digit = tag.contents[0]
    num = int(digit)
    count += 1
    total += num
print('Count:', count)
print('Sum:', total)
