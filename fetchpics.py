# Author: skynet
# E-mail: skynet.tw@gmail.com
# Date: 2015/9
# Programming Lanuage: Python 2.7
#
# Usage: Python fetchpics.py targetURL 
#
import requests
import shutil
from bs4 import BeautifulSoup
import sys, os

args = sys.argv
if len(args) < 2:
    print "Please enter a URL to fetch!"
    exit(0)
output_path = "pics/"
if not os.path.exists(output_path):
	os.mkdir(output_path)
turl = args[1]
res = requests.get(turl)
soup = BeautifulSoup(res.text, "html.parser")
count = 0
for img in soup.select('img'):
    fname =  img['src'].split('/')[-1]
    fname_length = len(fname)
    if '.jpg' in fname:
        if '?' in fname:
            real_fname = fname.split('?')[0]
        else:
            real_fname = fname
        real_fname = output_path + real_fname
        print real_fname
        res2 = requests.get(img['src'], stream=True)
        res_length = res2.headers['content-length']
        if int(res_length) < 50000: 
            print "--->Too small, discard it!"
            continue
        fp = open(real_fname, 'wb')
        shutil.copyfileobj(res2.raw,fp)
        fp.close()
        del res2
        count = count + 1
print "Total", count , " pictures done."
