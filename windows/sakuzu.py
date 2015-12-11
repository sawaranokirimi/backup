#coding: utf-8
import numpy as np
import math

# # # # # # 格子を描く関数 # # # # # # # # #
def draw_grid(genten, koushi, haba, f):
    f.write('newpath\n')
    for i in range(genten, genten + haba*koushi, haba):
        yokosen = str(genten) + ' ' + str(i) + ' moveto\n'
        yokosen = yokosen + str(genten + haba*(koushi-1)) + ' ' + str(i) + ' lineto\n'
        f.write(yokosen)

    for i in range(genten, genten + haba*koushi, haba):
        tatesen = str(i) + ' ' + str(genten) + ' moveto\n'
        tatesen = tatesen + str(i) + ' ' + str(genten + haba*(koushi-1)) + ' lineto\n'
        f.write(tatesen)

    f.write('stroke\n')

# # # # # # 円を描く関数 # # # # # # # # #
def draw_circle(x, y, r, f):
    circle = 'newpath\n'
    if r >= 0:
        circle += '1 0 0 setrgbcolor\n'
    else:
        circle += '0 0 1 setrgbcolor\n'

    circle += str(x) + ' ' + str(y) +  ' ' + str(r) +  ' 0 360 arc\n'
    circle_fill =  circle + 'fill\n'
    circle_stroke = circle + '0 setgray\n' + 'stroke\n'
    f.write(circle_fill)
    f.write(circle_stroke)


# # # # # # 作図ファイルの読み込み関数 # # # # # #
def open_file(name):
    name = name + '.eps'
    f = open(name, 'w')
    f.write('%%BoundingBox: 0 0 605 855\n')
    return f

# # # # # #  # 格子図の作図関数 # # # # # # # # # # # #
# # # # # n1,n2を用いた関数から作図 # # # # #
def mk_fig1(file_name, function):
    genten = 60#作図の原点（ｘ＝ｙ＝genten)
    koushi = 6#格子点の数
    haba = 60#格子の間隔
    jinko_keisu = haba*0.4#人口の係数（作図の都合上)

    f = open_file(file_name)
    draw_grid(genten, koushi, haba, f)
    for n1 in range(0, koushi, 1):
        for n2 in range(0, koushi, 1):
            jinko = math.copysign(math.sqrt(math.fabs(function(n1, n2))), function(n1, n2))
            draw_circle(genten + n1*haba, genten + (koushi-1-n2)*haba, jinko*jinko_keisu, f)
    f.write('showpage')
    f.close()

# # # # # 人口ベクトルを引数に作図 # # # # #
def mk_fig2(pop, keisu=0.5, file_name='out_pop'):
    genten = 60#作図の原点（ｘ＝ｙ＝genten)
    koushi = 6#格子点の数
    haba = 60#格子の間隔
    jinko_keisu = haba*keisu#人口の係数（作図の都合上)

    f = open_file(file_name)
    draw_grid(genten, koushi, haba, f)
    for n1 in range(0, koushi, 1):
        for n2 in range(0, koushi, 1):
            jinko = math.copysign(math.sqrt(math.fabs(pop[n2*koushi + n1])),pop[n2*koushi + n1])
            draw_circle(genten + n1*haba, genten + (koushi-1-n2)*haba, jinko*jinko_keisu, f)
    f.write('showpage')
    f.close()

if __name__ == '__main__':
    import eng_func as eng

    mk_fig1('tameshi', eng.Q2and3_1)
#    mk_fig1('Q2and3_2', eng.Q2and3_2)
#    mk_fig1('Q2and3_3', eng.Q2and3_3)
#    mk_fig1('Q2and3_4', eng.Q2and3_4)
