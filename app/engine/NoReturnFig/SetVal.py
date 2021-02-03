from ..ReturnFig.ReturnFig import ReturnFig
from .NoReturnFig import NoReturnFig


class SetVal(NoReturnFig):
    var_name:str
    # 值或值的表达式
    value_exp:ReturnFig