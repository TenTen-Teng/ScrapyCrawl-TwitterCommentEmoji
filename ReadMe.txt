爬虫程序在TwComment -> spiders -> twComment.py

在twComment.py里有start_requests函数里的urls是起始网址， 第一个备注上的是twitter首页的实时状态的网址，第二个urls是一些著名的人的twitter，如果想改所爬的网址，改这个urls就行

最后生成的文件是json格式的，存在TwComment文件下，名称是results.json

