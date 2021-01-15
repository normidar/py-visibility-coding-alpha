import pickle as pk
from app.engine.NoReturnFig.Project import Project


class Saver(object):
    
    @staticmethod
    def from_file_to_object(path: str):
        a = Saver.new_instance("Project",**{"a":"b"})
        print(a.a)
        print(a.__class__.__name__)

    @staticmethod
    def new_instance(cls_name,**kwargs):
        instance = eval(cls_name + "()")
        instance.__dict__ = kwargs
        return instance
    
    @staticmethod
    def run():
        Pickler.to_file(Project(a="abc"),"output.bt")
        obj = Pickler.from_file("output.bt")
        print(obj.a)

class Pickler(object):
    @staticmethod
    def to_file(obj,path: str):
        with open(path,"wb") as f:
            pk.dump(obj,f)

    @staticmethod
    def from_file(path:str):
        with open(path,"rb") as f:
            return pk.load(f)

Saver.run()
