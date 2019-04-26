import numpy as np

def print_cos(x):
    cosx = np.cos(np.radians(x))

    return f"This is the cos of {x}: %.10f" % cosx
