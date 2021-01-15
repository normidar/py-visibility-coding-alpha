from app import *

data = Project()

code1 = Var(var_name="a",var_type="int")
code2 = SetVal(var_name="a",value_exp=Value(value=123))

p_codes = CodeList()
p_codes.codes = [code1,code2]
data.codes = p_codes

