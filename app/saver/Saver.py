import yaml
from app.engine.NoReturnFig.Project import Project


class Saver(object):
    # 从文件翻译到实例
    @staticmethod
    def from_file_to_object(path: str):
        obj = Saver.from_yaml_to_map(path)
        for i in obj.keys():
            a = Saver.new_instance(i,**obj[i])
        print(a.a)
        print(a.__class__.__name__)

    # 从yaml翻译到
    @staticmethod
    def from_yaml_to_map(path: str):
        with open(path) as f:
            obj = yaml.load(f)
            return obj

    @staticmethod
    def new_instance(cls_name,**kwargs):
        instance = eval(cls_name + "()")
        instance.__dict__ = kwargs
        return instance
    
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    @staticmethod
    def from_map_to_yaml(path: str,obj):
        with open(path, "w") as f:
            yaml.dump(obj, f)
    @staticmethod
    def run():
        pass 
        # Saver.from_file_to_object("input.yaml")
        # x = Saver.from_yaml_to_map("input.yaml")
        # print(x)
        # Saver.from_map_to_yaml("output.yaml",{"project":{"cls_name":"Project","codes":[{"cls0":{}}]}})

Saver.run()
