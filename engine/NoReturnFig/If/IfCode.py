from ..NoReturnFig import NoReturnFig
from ..CodeList import CodeList
from engine.ReturnFig.ReturnFig import ReturnFig


class IfCode(NoReturnFig):
    # 条件
    condition: ReturnFig
    codes: CodeList