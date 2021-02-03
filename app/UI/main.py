import tkinter.ttk as ttk
import tkinter as tk
import time
from app.engine.NoReturnFig.DefCls import DefCls
from app.engine.NoReturnFig.Project import Project
from app.engine.NoReturnFig.CodeList import CodeList
from app.engine.NoReturnFig.DefFunc import DefFunc

class Main:
    def __init__(self, master):
        self.master = master
        # self.frame = ttk.Frame(master,width=3900,height=1900)
        canvas = tk.Canvas(master, width=800, height=480, bg="gray")
        # LineH(canvas, 0, 100, 20)
        first = Rectangle(canvas, 10, 10)
        first.create_same().create_son().create_same().create_same() \
            .create_same().create_son().create_same().create_same() \
            .create_son()
        p = Tran(first).tran()
        print(p.codes.code_list[1].codes.code_list)
        # canvas.create_line(-30,0,30,100,fill="red")
        canvas.pack()

    def create_button(self):
        pass




class Image:
    pass


class LineH(Image):
    def __init__(self, canvas: tk.Canvas, x1, x2, y):
        self.canvas = canvas
        self.obj = canvas.create_line(x1, y, x2, y, width=2, fill="red")


class Rectangle:
    def __init__(self, canvas: tk.Canvas, x, y):
        self.son:Rectangle = None
        self.same:Rectangle = None
        self.canvas = canvas
        self.x = x
        self.y = y
        self.obj = canvas.create_rectangle(x, y, x + 200, y + 33, width=2, outline="yellow")

    def move(self, x, y):
        self.canvas.coords(self.obj, (x, y, x + 200, y + 33))
        self.x = x
        self.y = y
        return self

    def create_son(self):
        rt = Rectangle(self.canvas, self.x + 33, self.y + 33)
        self.son = rt
        return rt

    def create_same(self):
        rt = Rectangle(self.canvas, self.x, self.y + 33)
        self.same = rt
        return rt

    def delete(self):
        self.canvas.delete(self.obj)


class Tran:
    def __init__(self, rectangle:Rectangle):
        self.rectangle = rectangle

    def tran(self):
        cl = CodeList
        p = Project(codes=cl)
        #
        rect = self.rectangle
        while rect:
            cls = DefCls(class_name="A")
            cl.code_list.append(cls)
            son = rect.son
            while son:
                # funcを入れる
                cls.codes.code_list.append(DefFunc(function_name="a"))
                son = son.same
            rect = rect.same
        return p
