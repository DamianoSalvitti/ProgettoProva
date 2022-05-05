import sys
import os

# Reach the parent's path
f_path = os.path.dirname(__file__)
parent_path = os.path.join(f_path, '..')
sys.path.append(os.path.abspath(parent_path))

# Import of the desired module
from src.compute_flask_cv.compute import *

# Test
if __name__ == '__main__':

    # Module correctly imported 
    print('"compute" imported correctly.')
    print('Start testing "compute.py"\n')

    # Input - add_one
    add = float(input('Inserte the number to be tested with "add_one": '))

    # Test - add_one
    res_add = add_one(add)
    print(f'Add 1 to {add} -> {res_add}\n')

    # Input - x_times_y
    times = input('Insert 2 numbers ("n1, n2") to be tested with "x_times_y": ')

    # Test - x_times_y
    times = times.split(sep=',')
    times0 = float(times[0])
    times1 = float(times[1])
    res_times = x_times_y(times0,times1)
    print(f'Multiply {times0} and {times1} -> {res_times}')
