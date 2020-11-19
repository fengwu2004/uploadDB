import time
from data.securities import Securities
from data.klineModel import KLineModel

def getLines(file):

    lines = [line.rstrip('\n') for line in open(file, 'r+', encoding='gbk')]

    lines.pop(1)

    lines.pop()
    
    return lines

def getTime(value:int):
    
    return value

def formatData(lines) -> Securities:
    
    stock = Securities()
    
    if len(lines) > 1:
        
        values = lines[0].split(' ')
        
        stock.code = values[0]
        
        i = 1
        
        while values[i] != '日线':
        
            stock.name += values[i]
            
            i += 1
        
        lines.pop(0)

    if len(lines) <= 1:
        
        return stock
    
    preClose = 0

    for line in lines:
        
        kline = KLineModel()
    
        values = line.split('\t')

        if int(values[0]) < 20161230:
            
            continue
        
        kline.preClose = preClose
        
        kline.date = int(values[0])

        kline.open = float(values[1])

        kline.high = float(values[2])

        kline.low = float(values[3])

        kline.close = float(values[4])

        kline.tradeamount = float(values[5])

        kline.tradevolume = float(values[6])

        stock.klines.append(kline)

        preClose = kline.close
        
    return stock