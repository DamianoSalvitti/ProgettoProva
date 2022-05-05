import sys, os
f_path = os.path.dirname(__file__)
parent_path = os.path.join(f_path, '..')
sys.path.append(os.path.abspath(parent_path))

from src.example_package.opencv_example import *

if __name__ == '__main__':
    print('Modulo "opencv_example" importato correttamente.')
    print('Avvio test del modulo "opencv_example.py"\n')
