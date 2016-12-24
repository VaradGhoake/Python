import urllib
from bs4 import BeautifulSoup

import os
proxy = 'specify proxy here'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

for j in range(1, *pages):
    req = urllib.urlopen("http://www.geeksforgeeks.org/category/*category/") #+  str(j) + "/")*multiple pages
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
    try:
        file_to_write = open("Graphs" + str(j) + ".txt", 'w')
    except(AttributeError):
        print "Error"
    for que, info in pairs.items():
    	file_to_write.write(que.encode('ascii', 'ignore') + '\n')
    	file_to_write.write( '\t' + info.encode('ascii', 'ignore') + '\n\n\n\n')

    print "Saved to the file no. =" + str(j)
    file_to_write.close()
