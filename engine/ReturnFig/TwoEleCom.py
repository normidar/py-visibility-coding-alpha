from .ReturnFig import ReturnFig

# 所有的二元运算(+-*/<>^or and%等等)
class TwoEleCom(ReturnFig):
    first_element:ReturnFig
    second_element:ReturnFig
    compute_type:str
