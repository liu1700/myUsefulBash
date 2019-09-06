# -*- coding:utf-8 -*-

import glob
import os
from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()

rawPath = './raw_stock_data'
convertedPath = './converted_stock_data'
for filename in glob.glob(rawPath+'/*.csv'):
    print(filename.ljust(60))
    detector.reset()
    with open(filename,'rb') as f:
        for line in f.readlines():
            detector.feed(line)
            if detector.done: break
        detector.close()
        print (detector.result)

        baseName = os.path.basename(filename)
        f1 = open(filename, 'rb')
        content = f1.read().decode(detector.result['encoding'].lower())
        f1.close()
        f1 = open(convertedPath+'/'+baseName, 'wb')
        f1.write(content.encode('utf-8'))
        f1.close()
