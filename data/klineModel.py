class KLineModel(object):
    
    def __init__(self):

        self.open = 0

        self.close = 0

        self.preClose = 0

        self.low = 0

        self.high = 0

        self.index = 0

        self.date:int = 19991230

        self.tradeamount = 0

        self.tradevolume = 0

    def greateChangeRatio(self) -> bool:

        if self.preClose == 0:

            return False

        return abs(self.close - self.preClose)/self.preClose > 0.080

    def limitup(self) -> bool:

        if self.preClose == 0:

            return False

        return (self.close - self.preClose)/self.preClose > 0.095

    def limitdown(self) -> bool:

        if self.preClose == 0:

            return False

        return abs(self.close - self.preClose)/self.preClose > 0.095

    def isHammer(self):

        return self.isHammer_green() or self.isHammer_red()

    def isHammer_red(self):

        if self.close < self.open:

            return False

        if (self.high - self.low)/self.open < 0.06:

            return False

        if self.open - self.close != 0 and (self.open - self.low)/(self.close - self.open) < 2:

            return False

        if (self.high - self.open)/(self.high - self.low) > 0.33:

            return False

        return True

    def isHammer_green(self):

        if self.open < self.close:

            return False

        if (self.high - self.low)/self.open < 0.06:

            return False

        if self.open - self.close != 0 and (self.close - self.low)/(self.open - self.close) < 2:

            return False

        if (self.high - self.close) / (self.high - self.low) > 0.33:

            return False

        return True

    def toJson(self):

        return {
            "preClose":self.preClose,
            'Open':self.open,
            'Close':self.close,
            'Low': self.low,
            'High': self.high,
            'Date': self.date,
            'tradeamount': self.tradeamount,
            'Volume': self.tradevolume,
        }

    @classmethod
    def fromJson(cls, jsonvalue):

        obj = KLineModel()

        obj.preClose = jsonvalue['preClose']

        obj.open = jsonvalue['Open']

        obj.close = jsonvalue['Close']

        obj.low = jsonvalue['Low']

        obj.high = jsonvalue['High']

        obj.date = jsonvalue['Date']

        obj.tradeamount = jsonvalue['tradeamount']

        obj.tradevolume = jsonvalue['Volume']

        return obj

