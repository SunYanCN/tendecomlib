from ..tensor import tensor
import numpy as np

def tenzeros(shp):
    data = np.ndarray(shp).fill(0)
    return tensor(data,shp)

def tenones(shp):
    data = np.ndarray(shp).fill(1)
    return tensor(data,shp)