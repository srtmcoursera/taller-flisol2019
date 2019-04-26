import numpy as np

def print_sin(x):
    sinx = np.sin(np.radians(x))

    return f"This is the sin of {x}: %.10f" % sinx
