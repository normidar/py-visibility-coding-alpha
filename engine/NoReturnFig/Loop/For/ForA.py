from ...NoReturnFig import NoReturnFig
from ...CodeList import CodeList

class ForA(NoReturnFig):
    start: int
    # 不包含
    end: int
    step: int
    # 变量名
    index_name: str
    codes: CodeList