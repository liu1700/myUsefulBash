#!/usr/bin/python
import time
import json
import urllib.request

with open('./get.json') as json_file:
    data = json.load(json_file)
    data = data['data']
    for p in data['diff']:
        time.sleep(3)
        print('Start downloading Security: ' + p['f12'])

        urllib.request.urlretrieve('http://quotes.money.163.com/service/chddata.html?code=0'+p['f12']+'&start=19901219&end=20190905&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER', './'+p['f12']+'.csv')
