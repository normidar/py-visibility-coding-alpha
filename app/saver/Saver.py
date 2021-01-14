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
        Saver.from_file_to_object("")

Saver.run()
