import math

def print_sin(x):
    sinx = math.sin(math.radians(x))

    return f"This is the sin of {x}: %.10f" % sinx
