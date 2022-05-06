import sys
import os

# Reach the root's path
f_path = os.path.dirname(__file__)
root_path = os.path.join(f_path, os.pardir)
sys.path.append(os.path.abspath(root_path))

# Import of the desired module
import src.compute_flask_cv.compute as cmp

# Test
if __name__ == '__main__':

    # Module correctly imported 
    print('"compute" imported correctly.')
    print('Start testing "compute.py"\n')

    # Input - add_one
    add = float(input('Inserte the number to be tested with "add_one": '))

    # Test - add_one
    res_add = cmp.add_one(add)
    print(f'Add 1 to {add} -> {res_add}\n')

    # Input - x_times_y
    times = input('Insert 2 numbers ("n1, n2") to be tested with "x_times_y": ')

    # Test - x_times_y
    times = times.split(sep=',')
    times0 = float(times[0])
    times1 = float(times[1])
    res_times = cmp.x_times_y(times0,times1)
    print(f'Multiply {times0} and {times1} -> {res_times}')
