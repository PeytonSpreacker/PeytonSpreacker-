import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL: ')

if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_1501843.xml'
print("Retrieving", url)

data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters.')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count:', len(counts))

tot = list()

for i in counts:
    num = int(i.text)
    tot.append(num)

print('Sum:', sum(tot))