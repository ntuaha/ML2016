import numpy as np
import sys

def parse(path,col_index):
    data = np.genfromtxt(path, delimiter=' ')
    dt = [('f%d'%(i+1),np.float64) for i in range(data.shape[1])]
    out = np.sort(data.view(dtype=dt),order=['f%d'%col_index],axis=0).view(np.float64)
    np.savetxt("ans1.txt", out, delimiter=",",fmt="%.5f")


if __name__ == "__main__":
    parse(sys.argv[2],int(sys.argv[1]))
    