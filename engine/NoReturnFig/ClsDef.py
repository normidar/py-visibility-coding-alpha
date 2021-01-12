from .NoReturnFig import NoReturnFig
from .CodeList import CodeList


# 类
class ClsDef(NoReturnFig):
    class_name: str
    father_name: str
    # 接口
    interface_names: list
    visible_type: str
    # 定义区代码
    codes: CodeList
    # 构造函数
    # 函数群
