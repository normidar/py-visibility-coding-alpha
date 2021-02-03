from .CodeList import CodeList
from .DefFunc import DefFunc
from .NoReturnFig import NoReturnFig


# 类
class DefCls(NoReturnFig):
    class_name: str
    # 父类名
    father_names: list
    # 接口
    interface_names: list
    visible_type: str
    # 定义区代码
    codes: CodeList = CodeList()
    # 构造函数
    cls_method: DefFunc
    # 函数群
    methods: list # <DefFunc>
