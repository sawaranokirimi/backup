#coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import RectangleSelector

class RectSelect(object):
    def __init__(self, ax=None):
        self.ax = ax or plt.gca()
        self.rect = Rectangle((0,0), 0, 0, color='orange', alpha=0.5)
        self.ax.add_patch(self.rect)
        self.blc = np.zeros(2)
        self.trc = np.zeros(2)
        self.ax.set_aspect('equal')

        def selector(event):
            if event.key in ['Q', 'q'] and selector.RS.active:
                print ('RectSelect deactivated.')
                selector.RS.set_active(False)
            if event.key in ['A', 'a'] and not selector.RS.active:
                print ('RectSelect activated.')
                selector.RS.set_active(True)

        selector.RS = RectangleSelector(self.ax, self.callback)
        self.ax.figure.canvas.mpl_connect('key_press_event', selector)
        self.ax.figure.canvas.mpl_connect('button_release_event', self.release)

    def callback(self, eclick, erelease):
        x0, x1 = eclick.xdata, erelease.xdata
        y0, y1 = eclick.ydata, eclick.ydata + np.abs(x1-x0)*np.sign(erelease.ydata-eclick.ydata)
        self.blc = min(x0, x1), min(y0, y1)
        self.trc = max(x0, x1), max(y0, y1)
        blc_print = '({:0.4},{:0.4})'.format(*self.blc)
        trc_print = '({:0.4},{:0.4})'.format(*self.trc)
        print('blc={}, trc={}'.format(blc_print, trc_print))

    def release(self, event):
        self.rect.set_width(self.trc[0] - self.blc[0])
        self.rect.set_height(self.trc[0] - self.blc[0])
        self.rect.set_xy(self.blc)
        self.ax.figure.canvas.draw()

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
#    from rectselect import RectSelect
    #   何かプロット
    x = [0, 1, 2, 3, 4, 5, 6, 7]
    y = [0, 1, 2, 3, 4, 5, 6, 7]
#    plt.plot(x,y,'.')
    plt.scatter(x, y, s=(100*np.random.rand(8))**2, alpha=0.5)
    # ボックス選択
    region = RectSelect()
    plt.show()
    # ボックスの左下(blc)と右上(trc)の座標を表示
    print(region.blc) # --> (2.338709677419355, 3.7239583333333335)
    print(region.trc) # --> (8.4879032258064502, 8.671875)
