from tkinter import *
import tkinter.ttk as ttk
import math

class ButtonSampleMove(ttk.Frame):
    points = {(0,0),(0,100)}
    def __init__(self, master):
        super().__init__(master,width=3900,height=1900)
        self.start_xy = None
        self.x_y  = None
        self.create_widgets()
        self.propagate(False)
        self.pack()

    def create_widgets(self):
        button = ttk.Button(self,text = "if")
        button.place(x=640,y=50)
        button.config(width=15)
        self.bind_widget(button)

        button = ttk.Button(self,text = "buttonB")
        button.place(x=640,y=100)
        self.bind_widget(button)

    def bind_widget(self,widget):
        widget.bind("<Button-1>",self.move_start)
        widget.bind("<B1-Motion>",self.move_now)
        widget.bind("<ButtonRelease-1>",self.move_end)

    def move_start(self,event):
        # マウスカーソルの座標取得
        self.start_xy = (event.x_root,event.y_root)
        # 位置情報取得
        place_info = event.widget.place_info()
        x = int(place_info['x'])
        y = int(place_info['y'])
        self.x_y = (x,y)

    def move_now(self,event):
        if self.start_xy is None:
            return
        # 移動距離を調べる
        distance = (event.x_root-self.start_xy[0],event.y_root-self.start_xy[1])
        # 再度座標を設定する
        place_info = event.widget.place_info()
        place_info['x'] = self.x_y[0] + distance[0]
        place_info['y'] = self.x_y[1] + distance[1]
        event.widget.place_configure(place_info)

    def move_end(self,event):
        # 磁石
        place_info = event.widget.place_info()
        point = (int(place_info['x']),int(place_info['y']))
        # 一番近い点を探す
        min_len = 10000
        min_point = (10000,10000)
        for p in self.points:
            v = (point[0] - p[0]),(point[1] - p[1])
            le = math.sqrt(v[0]**2 + v[1]**2)
            if le < min_len:
                min_len = le
                min_point = p
        # 磁上
        place_info['x'] = min_point[0]
        place_info['y'] = min_point[1]
        event.widget.place_configure(place_info)
        # 点下移
        self.points.remove(min_point)
        self.points.add((min_point[0], min_point[1]+25))
        # 座標類を初期化
        self.start_xy = None
        self.x_y = None

import main as main

if __name__ == '__main__':
    master = Tk()
    master.title("ButtonSampleMove")
    # master.geometry("800x480")
    main.Main(master)
    master.mainloop()

