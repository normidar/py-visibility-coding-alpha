from .NoReturnFig import NoReturnFig
from engine.ReturnFig.ReturnFig import ReturnFig

class SetVal(NoReturnFig):
    var_name:str
    # 值或值的表达式
    value_exp:ReturnFig