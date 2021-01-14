from .NoReturnFig import NoReturnFig
from engine.ReturnFig.ReturnFig import ReturnFig

class Var(NoReturnFig):
    var_name:str
    cls_name:str
    # 值或值的表达式
    value_exp:ReturnFig