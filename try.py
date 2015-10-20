#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

class DraggableRectangle:
    def __init__(self, rect):
        self.rect = rect
        self.press = None

    def connect(self):
        self.cidpress = self.rect.figure.canvas.mpl_connect(
                'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
                'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
                'motion_notify_event', self.on_motion)
        
    def on_press(self, event):       
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(self)
        if not contains:
            return
        print 'event contains', self.rect.xy
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata
        
    def on_motion(self, event):
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)

        self.rect.figure.canvas.draw()

    def on_release(self, event):
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        
    
fig = plt.figure()
ax = fig.add_subplot(111)
rects = ax.bar(range(10), 20*np.random.rand(10))
drs = []
for rect in rects:
    dr = DraggableRectangle(rect)
    dr.connect()
    drs.append(dr)

plt.show()

