from ...NoReturnFig import NoReturnFig
from ...CodeList import CodeList
from ....ReturnFig import ReturnFig

class ForC(NoReturnFig):
    # 变量名
    index_name: str
    # 数组,链表的表达式
    array_exp: ReturnFig
    # 代码
    codes: CodeList
    