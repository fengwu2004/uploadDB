from os import walk
from data.codeInfo import CodeInfo
from storemgr.load import getLines, formatData
from data.databasemgr import DatabaseMgr
import json
from collections import defaultdict

def saveToDB():
    
    mypath = 'C:/Users/Administrator/Desktop/tdx-gbk/'
    
    f = []
    
    for (dirpath, dirname, filenames) in walk(mypath):
        
        f.extend(filenames)
    
    print(f)

    stocks = []
    
    for file in f:

        filePath = mypath + file
        
        if filePath.find('.txt') == -1:
            
            continue
        
        stock = formatData(getLines(filePath))
    
        stocks.append(stock.toJson())

    DatabaseMgr.instance().stocks.remove({})

    DatabaseMgr.instance().stocks.insert_many(stocks)

    result = []

    for stock in stocks:

        codeInfo = CodeInfo()

        codeInfo.code = stock['code']

        codeInfo.name = stock['name']

        result.append(codeInfo.toJson())

    DatabaseMgr.instance().stockInfos.remove({})

    DatabaseMgr.instance().stockInfos.insert_many(result)

saveToDB()