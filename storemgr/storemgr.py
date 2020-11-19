from datetime import datetime

from data.securities import Securities
from data.klineModel import KLineModel
from data.databasemgr import DatabaseMgr
from data.codeInfo import CodeInfo
from data.block import BlockInfo
from typing import Dict, List
import tushare as ts

abortBlocks = {
    "送转预期",
    "ETC",
    "成渝特区",
    "QFII重仓",
    "深圳特区",
    "独角兽",
    "智慧城市",
    "富时概念",
    "雄安新区",
    "创业成份",
    "增强现实",
    "MSCI中国",
    "2025规划",
    "昨日触板",
    "移动支付",
    "券商概念",
    "风能",
    "IPv6",
    "HS300",
    "中超概念",
    "租售同权",
    "基金重仓",
    "养老概念",
    "MSCI大盘",
    "股权激励",
    "UWB概念",
    "中字头",
    "创业板综",
    "上证180",
    "标普概念",
    "股权转让",
    "昨日涨停",
    "深成500",
    "创投",
    "地热能",
    "二胎概念",
    "北京冬奥",
    "海绵城市",
    "小米概念",
    "预亏预减",
    "参股保险",
    "智能家居",
    "深成500",
    "粤港自贸",
    "无人驾驶",
    "阿里概念",
    "国企改革",
    "WiFi",
    "新三板",
    "降解塑料",
    "影视概念",
    "手游概念",
    "高校",
    "苹果概念",
    "PPP模式",
    "健康中国",
    "京津冀",
    "滨海新区",
    "智能电视",
    "深证100R",
    "上证50",
    "智能穿戴",
    "可燃冰",
    "智慧政务",
    "纳米银",
    "京东金融",
    "养老金",
    "百度概念",
    "美丽中国",
    "东北振兴",
    "富士康",
    "万达概念",
    "证金持股",
    "创业板壳",
    "IPO受益", 
    "长江三角",
    "举牌概念",
    "沪股通", 
    "中证500",
    "壳资源",
    "MSCI中盘",
    "虚拟现实",
    "预盈预增",
    "养老金",
    "共享经济",
    "参股券商",
    "深圳特区",
    "高送转", "上证380", "转债标的", "融资融券", "贬值受益", "昨日连板", "分拆预期", "机构重仓", "ST概念", "深股通", "债转股", "AH股", "AB股", "创业板壳"}

def loadCapitalsFromDB() -> Dict:

    result:Dict = {}

    items = DatabaseMgr.instance().capitals.find({}, {'_id': 0})

    for item in items:

        capital = int(item["capital"])

        result[item["code"]] = capital

    return result

def loadAllSecuritiesFromDB() -> List[Securities]:

    result:List[Securities] = []

    items = DatabaseMgr.instance().stocks.find({}, {'_id': 0})

    for item in items:

        if 'code' in item:

            code = item['code']

            if code == 0:

                continue

            securities = Securities.fromJson(item)

            securities.calcMinsAndMaxs()

            result.append(securities)

    return result

def loadAllBlockFromDB() -> List[BlockInfo]:
    
    result:List[BlockInfo] = []

    items = DatabaseMgr.instance().block.find({}, {'_id': 0})

    for item in items:

        if 'name' in item and "codeList" in item:

            name = item['name']

            codeList = item['codeList']

            if name is None or name in abortBlocks:

                continue

            blockInfo = BlockInfo()

            blockInfo.createFromJson(name, codeList)

            result.append(blockInfo)

    return result

_instance = None
class SecuritiesMgr(object):

    @classmethod
    def instance(cls):

        global _instance

        if _instance is None:

            _instance = SecuritiesMgr()

        return _instance

    def __init__(self):
    
        self.securitiesList:List[Securities] = list()

        self.blockList:List[BlockInfo] = list()

        self.date = None

        self.capitals:Dict = None

        self.stockbasic = None

        self.loadSecuritiess()

        super().__init__()

    def loadSecuritiess(self):

        d = datetime.now().timestamp()

        self.date = datetime.now().strftime('%Y%m%d')

        self.capitals = loadCapitalsFromDB()

        print("开始加载" , datetime.now())

        self.securitiesList = loadAllSecuritiesFromDB()

        print("结束加载", datetime.now())

        for securities in self.securitiesList:

            if securities.codeInfo.code in self.capitals:

                securities.capital = self.capitals[securities.codeInfo.code]

        self.blockList = loadAllBlockFromDB()

        self.stockbasic = ts.get_stock_basics()

    def getSecurities(self, codeInfo:CodeInfo) ->Securities:

        for securities in self.securitiesList:

            if securities.codeInfo == codeInfo:

                return securities

        return None

loadAllBlockFromDB()