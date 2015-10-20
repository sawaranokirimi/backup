import numpy as np
import pandas as pd








def main1():
    data = pd.read_csv('in_data.csv').values
    P = np.array([[1.0, -1.0/2.0],
                 [0.0, 3.0**(1/2.0)/2.0]])
    print data
    print P

    x = data[0:, 0:2].T
    obli_x = np.linalg.solve(P, x)
    print x, '\n', obli_x
if __name__ == '__main__':
    main1()

