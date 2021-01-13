from ...NoReturnFig import NoReturnFig
from ...CodeList import CodeList
from ....ReturnFig import ReturnFig

class ForB(NoReturnFig):
    # 定义
    def_code: NoReturnFig
    # 条件
    condition: ReturnFig
    # 每步执行
    step_code: NoReturnFig
    # 代码
    codes: CodeList
