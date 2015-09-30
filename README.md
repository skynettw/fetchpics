Program Name: fetchpics.py
Author: skynet
E-mail: skynet.tw@gmail.com
Date: 2015/9
Programming Language: Python 2.7

這是一個由Python所撰寫的簡易下載網頁圖片的程式，
沒有特定的使用對象，只要是有一大堆圖片連結的網頁，
也許你就可以使用這個程式來試試看。

使用方法：

Python fetchpics.py URL

其中，URL就是你要下載圖片的網頁網址。所有下載成功的圖片，都會被集中放置在pics的資料夾中。在程式中有特別把小於50000Byte的圖形檔略過不存，如果你覺得需要，請自行到程式中修改即可。

要順利執行此程式，需要安裝 requests 和 BeautifulSoup4
