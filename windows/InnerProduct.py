#coding: utf-8
import numpy as np
import pandas as pd
import os
import plot2
import sakuzu


os.chdir('../03')


# # # # # 座標変換行列の作成 # # # # #
class MatrixZ:
    def __init__(self, jinko):
        self.jinko = np.float64(jinko)
        self.jinko_num = self.jinko.shape[0]
        self.vec_num = 36#　要変更！！！！！

    def Q1_1(self, n1, n2):
        return 1.0
    def Q2_1(self, n1, n2):
        return np.cos(2.0*np.pi*n1/2)
    def Q2_2(self, n1, n2):
        return np.cos(2.0*np.pi*n2/2)
    def Q2_3(self, n1, n2):
        return np.cos(2*np.pi*(n1/2.0+n2/2.0))

    def Q3_1(self, n1, n2):
        return np.cos(2*np.pi*(n1/3.0))
    def Q3_2(self, n1, n2):
        return np.sin(2*np.pi*(n1/3.0))
    def Q3_3(self, n1, n2):
        return np.cos(2*np.pi*(n2/3.0))
    def Q3_4(self, n1, n2):
        return np.sin(2*np.pi*(n2/3.0))
    def Q3_5(self, n1, n2):
        return np.cos(2*np.pi*(n1/3.0+n2/3.0))
    def Q3_6(self, n1, n2):
        return np.sin(2*np.pi*(n1/3.0+n2/3.0))
    def Q3_7(self, n1, n2):
        return np.cos(2*np.pi*(n1/3.0-n2/3.0))
    def Q3_8(self, n1, n2):
        return np.sin(2*np.pi*(n1/3.0-n2/3.0))

    def Q6_1(self, n1, n2):
        return np.cos(2*np.pi*(n1/6.0))
    def Q6_2(self, n1, n2):
        return np.sin(2*np.pi*(n1/6.0))
    def Q6_3(self, n1, n2):
        return np.cos(2*np.pi*(n2/6.0))
    def Q6_4(self, n1, n2):
        return np.sin(2*np.pi*(n2/6.0))
    def Q6_5(self, n1, n2):
        return np.cos(2*np.pi*(n1/6.0+n2/6.0))
    def Q6_6(self, n1, n2):
        return np.sin(2*np.pi*(n1/6.0+n2/6.0))
    def Q6_7(self, n1, n2):
        return np.cos(2*np.pi*(n1/6.0-n2/6.0))
    def Q6_8(self, n1, n2):
        return np.sin(2*np.pi*(n1/6.0-n2/6.0))

    def Q2and3_1(self, n1, n2):
        return np.cos(2*np.pi*(n1/2.0+n2/3.0))
    def Q2and3_2(self, n1, n2):
        return np.sin(2*np.pi*(n1/2.0+n2/3.0))
    def Q2and3_3(self, n1, n2):
        return np.cos(2*np.pi*(n1/3.0+n2/2.0))
    def Q2and3_4(self, n1, n2):
        return np.sin(2*np.pi*(n1/3.0+n2/2.0))

    def Q2and6_1(self, n1, n2):
        return np.cos(2*np.pi*(n1/2.0+n2/6.0))
    def Q2and6_2(self, n1, n2):
        return np.sin(2*np.pi*(n1/2.0+n2/6.0))
    def Q2and6_3(self, n1, n2):
        return np.cos(2*np.pi*(n1/6.0+n2/2.0))
    def Q2and6_4(self, n1, n2):
        return np.sin(2*np.pi*(n1/6.0+n2/2.0))

    def Q3and6_1(self, n1, n2):
        return np.cos(2*np.pi*(n1/3.0+n2/6.0))
    def Q3and6_2(self, n1, n2):
        return np.sin(2*np.pi*(n1/3.0+n2/6.0))
    def Q3and6_3(self, n1, n2):
        return np.cos(2*np.pi*(n1/6.0+n2/3.0))
    def Q3and6_4(self, n1, n2):
        return np.sin(2*np.pi*(n1/6.0+n2/3.0))
    def Q3and6_5(self, n1, n2):
        return np.cos(2*np.pi*(n1/6.0-n2/3.0))
    def Q3and6_6(self, n1, n2):
        return np.sin(2*np.pi*(n1/6.0-n2/3.0))
    def Q3and6_7(self, n1, n2):
        return np.cos(2*np.pi*(n1/3.0-n2/6.0))
    def Q3and6_8(self, n1, n2):
        return np.sin(2*np.pi*(n1/3.0-n2/6.0))

    def to_tex(self, text):
        col = []
        for content in text:
            temp = '$' + content + '$'
            col.append(r'%s' % temp)
        return col

    def mk_col_name(self):
        col_name = pd.read_csv('in_columns.csv')
        return self.to_tex(col_name['vector name'])

    def mk_Z(self):
        Z = np.zeros((self.jinko_num, self.vec_num))

        for i in range(int(self.jinko_num**(0.5))):
            for j in range(int(self.jinko_num**(0.5))):
                Z[6*i+j, 0] = self.Q1_1(i, j)
                Z[6*i+j, 1] = self.Q2_1(i, j)
                Z[6*i+j, 2] = self.Q2_2(i, j)
                Z[6*i+j, 3] = self.Q2_3(i, j)
                Z[6*i+j, 4] = self.Q3_1(i, j)
                Z[6*i+j, 5] = self.Q3_2(i, j)
                Z[6*i+j, 6] = self.Q3_3(i, j)
                Z[6*i+j, 7] = self.Q3_4(i, j)
                Z[6*i+j, 8] = self.Q3_5(i, j)
                Z[6*i+j, 9] = self.Q3_6(i, j)
                Z[6*i+j, 10] = self.Q3_7(i, j)
                Z[6*i+j, 11] = self.Q3_8(i, j)
                Z[6*i+j, 12] = self.Q6_1(i, j)
                Z[6*i+j, 13] = self.Q6_2(i, j)
                Z[6*i+j, 14] = self.Q6_3(i, j)
                Z[6*i+j, 15] = self.Q6_4(i, j)
                Z[6*i+j, 16] = self.Q6_5(i, j)
                Z[6*i+j, 17] = self.Q6_6(i, j)
                Z[6*i+j, 18] = self.Q6_7(i, j)
                Z[6*i+j, 19] = self.Q6_8(i, j)
                Z[6*i+j, 20] = self.Q2and3_1(i, j)
                Z[6*i+j, 21] = self.Q2and3_2(i, j)
                Z[6*i+j, 22] = self.Q2and3_3(i, j)
                Z[6*i+j, 23] = self.Q2and3_4(i, j)
                Z[6*i+j, 24] = self.Q2and6_1(i, j)
                Z[6*i+j, 25] = self.Q2and6_2(i, j)
                Z[6*i+j, 26] = self.Q2and6_3(i, j)
                Z[6*i+j, 27] = self.Q2and6_4(i, j)
                Z[6*i+j, 28] = self.Q3and6_1(i, j)
                Z[6*i+j, 29] = self.Q3and6_2(i, j)
                Z[6*i+j, 30] = self.Q3and6_3(i, j)
                Z[6*i+j, 31] = self.Q3and6_4(i, j)
                Z[6*i+j, 32] = self.Q3and6_5(i, j)
                Z[6*i+j, 33] = self.Q3and6_6(i, j)
                Z[6*i+j, 34] = self.Q3and6_7(i, j)
                Z[6*i+j, 35] = self.Q3and6_8(i, j)

        for i in range(Z.shape[1]):
            Z[:, i]  = Z[:, i] / np.linalg.norm(Z[:, i])

        return Z


    def analize(self):
        sakuzu.mk_fig2(self.jinko)
        p = np.linalg.solve(self.mk_Z(), self.jinko/np.linalg.norm(self.jinko))
        return p

    def distribution(self):
        x = np.zeros((self.jinko_num, self.vec_num))
        Z = self.mk_Z()
        p = self.analize()
        for i in range(self.vec_num):
            x[:, i] = p[i] * Z[:, i]
        return x

    def norm(self):
        norm = np.zeros(10)
        P = self.analize()**2 #係数pの2乗

        def sumation(X, num1, num2):
            temp = 0.0
            for i in range(num1, num2 + 1):
                temp += X[i]
            return temp

        norm[0] = np.sqrt(P[0])
        norm[1] = np.sqrt(P[1] + P[2])
        norm[2] = np.sqrt(P[3])
        norm[3] = np.sqrt(sumation(P, 4, 7))
        norm[4] = np.sqrt(sumation(P, 8, 11))
        norm[5] = np.sqrt(sumation(P, 12, 15))
        norm[6] = np.sqrt(sumation(P, 16, 19))
        norm[7] = np.sqrt(sumation(P, 20, 23))
        norm[8] = np.sqrt(sumation(P, 24, 27))
        norm[9] = np.sqrt(sumation(P, 28, 35))

        return norm

    def col_norm(self):
        col = ['(1, 1)', '(2, 1)', '(2, 2)', '(3, 1)', '(3, 3)', '(6, 1)',
               '(6, 6)', '(2, 3)', '(2, 6)', '(3, 6)']
        return col


    def get_data(self):
        p = self.analize()
        x = self.distribution()
        norm = self.norm()

        print 'gyaku henkan \n', np.round(self.jinko, 10) == \
        np.round(np.dot(self.mk_Z(), p)*np.linalg.norm(self.jinko), 10)

        data_inpro = pd.Series(p, index = self.mk_col_name())
        data_inpro.to_csv('out_inner_product.csv')
        plot2.plot(p, self.mk_col_name())

        data_distribution = pd.DataFrame(x, columns = self.mk_col_name())
        data_distribution.to_csv('out_distribution.csv')

        plot2.GraphNorm('out_norm', norm, self.col_norm()).plot_norm()


if __name__ == '__main__':
    pop = np.array((pd.read_csv('in_pop.csv')['mono center'].dropna()))
    MatrixZ(pop).get_data()
