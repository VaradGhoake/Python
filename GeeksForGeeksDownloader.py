import urllib
from bs4 import BeautifulSoup

import os
proxy = 'http://111503022:ghodakevv15.comp_111503022@10.1.101.150:3128'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy


req = urllib.urlopen("http://www.geeksforgeeks.org/category/c-arrays/page/14/")
soup = BeautifulSoup(req.read())

tags = []
for a in soup.find_all(rel='bookmark'):
        tags.append(a.string)

child = []
i = 0
pairs = {'Key' : 'Value'}
for entry in soup.find_all("div", "entry-summary"):
        child = entry.contents
        pairs[tags[i]] = list(child[5])[0]
	i = i + 1

del pairs['Key']

file_to_write = open("Array14.txt", 'w')
for que, info in pairs.items():
	file_to_write.write(que.encode('ascii', 'ignore') + '\n')
	file_to_write.write( '\t' + info.encode('ascii', 'ignore') + '\n\n\n\n')

file_to_write.close()


