from ..NoReturnFig import NoReturnFig
from ..CodeList import CodeList
from engine.ReturnFig.ReturnFig import ReturnFig

class While(NoReturnFig):
    # 条件
    condition: ReturnFig
    codes: CodeList
