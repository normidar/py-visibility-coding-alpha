from .NoReturnFig import NoReturnFig
from .CodeList import CodeList

class DefFunc(NoReturnFig):
    function_name: str
    visible_type: str
    # 必选参数
    required_parameters: list #<Var>
    # 可选参数
    optional_parameters: list #<VarSet>
    # 返回类型
    return_type: str
    # 代码块
    codes: CodeList