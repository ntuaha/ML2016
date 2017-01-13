import numpy as np
from scipy import ndimage,misc
import sys

if __name__ == "__main__":
    misc.imsave('ans2.png', np.flipud(misc.imread(sys.argv[1])))