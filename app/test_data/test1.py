from app import *

data = Project()

code1 = Var(var_name="a",var_type="int")
code2 = SetVal(var_name="a",value_exp=Value(value=123))

p_codes = CodeList()
p_codes.code_list = [code1, code2]
data.code_list = p_codes

