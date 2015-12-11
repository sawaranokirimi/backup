#coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


mesh = 6

# lb: left, bottom | lt: left, top | rt: right, top | rb: right, bottom
class Parallel:
    def __init__(self, lb, lt, rt, rb, n=18):
        self.n = n
        self.lb = lb
        self.lt = lt
        self.rt = rt
        self.rb = rb
        self.verts = [lb, lt, rt, rb, (0., 0.)]

    def lattice_angle(self):                                                         
        return np.pi/6.0 - np.arctan((self.lt[1]-self.rb[1])/(self.rb[0]-self.lt[0]))

    def parallel_outline(self):
        codes = [Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO,
                Path.CLOSEPOLY,
                ]
        return Path(self.verts, codes)

    def parallel_grid(self):
        points = []
        codes = []
        haba = np.linalg.norm([self.lt[0]-self.rb[0],           
                               self.lt[1]-self.rb[1]])/np.sqrt(3)/(self.n-1)
        theta = self.lattice_angle()
        #　斜線のpath
        for i in range(1, self.n - 1):
            # x方向
            points.append((self.lb[0] + i*haba*np.cos(theta), 
                           self.lb[1] + i*haba*np.sin(theta)))
            points.append((self.lt[0] + i*haba*np.cos(theta), 
                           self.lt[1] + i*haba*np.sin(theta)))
            codes.append(Path.MOVETO)
            codes.append(Path.LINETO)
            # y方向
            points.append((self.lb[0] - i*haba*np.cos(np.pi/3.-theta),
                           self.lb[1] + i*haba*np.sin(np.pi/3.-theta)))
            points.append((self.rb[0] - i*haba*np.cos(np.pi/3.-theta),
                           self.rb[1] + i*haba*np.sin(np.pi/3.-theta)))
            codes.append(Path.MOVETO)
            codes.append(Path.LINETO)
            
        return Path(points, codes)


"""
verts = [
    (0., 0.), # left, bottom
    (0., 1.), # left, top
    (1., 1.), # right, top
    (1., 0.), # right, bottom
    (0., 0.), # ignored
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)
"""
if __name__ == '__main__':

    Point1 = (0., 0.) # left, bottom                                            
    Point2 = (-1., 1.7320508) # left, top                                  
    Point3 = (1., 1.7320508) # right, top                                 
    Point4 = (2., 0.) # right, bottom                                     
                                                                          
    path = Parallel(Point1, Point2, Point3, Point4).parallel_outline()    
    path_grid = Parallel(Point1, Point2, Point3, Point4).parallel_grid()  
    fig = plt.figure()                                                    
    ax = fig.add_subplot(111, aspect=1.0)                                 
    patch = patches.PathPatch(path, facecolor='orange', lw=2, alpha=0.4)  
    patch_grid = patches.PathPatch(path_grid, lw=1, alpha=0.4)            
    ax.add_patch(patch)                                                   
    ax.add_patch(patch_grid)                                              
    ax.set_xlim(-2,3.5)                                                   
    ax.set_ylim(-2,3)                                                     
    plt.show()                                                            
