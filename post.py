# -*- coding: utf-8 -*-
import requests
payload = {
'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
'EndStation':'a7a04c89-900b-4798-95a3-c01c455622f4',
'SearchDate':'2016/04/04',
'SearchTime':'20:00',
'SearchWay':'DepartureInMandarin'
}

res = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data=payload)
print res.text