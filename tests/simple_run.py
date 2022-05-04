import sys, os
f_path = os.path.dirname(__file__)
parent_path = os.path.join(f_path, '..')
sys.path.append(os.path.abspath(parent_path))

from src.example_package import example

def x_times_y (x, y):
    return x*y

if __name__ == '__main__':
    a = example.add_one(5)
    c = x_times_y(a,2)

    print('Modulo "example" importato correttamente.')
    print('"Hello from simple_run" come main!\n')
    print(f'Il risultato e\': {c}.')
