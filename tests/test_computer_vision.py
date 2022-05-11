import sys
import os
'''
# Reach the parent's path
f_path = os.path.dirname(__file__)
root_path = os.path.join(f_path, os.pardir)
sys.path.append(os.path.abspath(root_path))
'''
# Import of the desired module
import src.compute_flask_cv.computer_vision as cvn

# pytest
def test_eye_unit8():
    size = 5
    res_size = cvn.eye_unit8(size)
    
def test_rgb2gray():
    cwd = os.getcwd()
    path = os.path.join(cwd,"src","A_Cannone.jpg")
    gray, np_array_g = cvn.rgb2gray(path)
    cvn.cv2.destroyAllWindows()
    
def test_rgb2bgr():
    cwd = os.getcwd()
    path = os.path.join(cwd,"src","A_Cannone.jpg")
    bgr, np_array_b = cvn.rgb2bgr(path)
    cvn.cv2.destroyAllWindows()

# Test as main
if __name__ == '__main__':

    # Module correctly imported 
    print('"computer_vision" imported correctly.')
    print('Start testing "computer_vision.py"\n')

    # Input - eye_unit8
    size = int(input('Please insert the matrix dimension to be tested with "eye_unit8": '))

    # Test - eye_unit8
    res_size = cvn.eye_unit8(size)
    print(f'Dimension of the identity matrix: {size}')
    print(res_size)

    # Input - rgb2gray, rgb2bgr
    choice = input('\nChoose the number to have the converted photo created:\n' +
                   '1: RGB -> Gray scale\n' +
                   '2: RGB -> BRG\n')

    # Test - rgb2gray, rgb2bgr
    cwd = os.getcwd()
    path = os.path.join(cwd,os.pardir,"src","A_Cannone.jpg")
    match choice:
        case '1':
            gray, np_array_g = cvn.rgb2gray(path)
        case '2':
            bgr, np_array_b = cvn.rgb2bgr(path)
