from ..NoReturnFig import NoReturnFig
from ..CodeList import CodeList
from engine.ReturnFig.ReturnFig import ReturnFig


class ElseIfCode(NoReturnFig):
    condition: ReturnFig
    codes: CodeList