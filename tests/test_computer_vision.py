import os

# # Block avoided in order to test the "export PYTHONPATH=src"
# # command in the "applications-test.yml" file
# import sys
#
# # Reach the parent's path
# f_path = os.path.dirname(__file__)
# root_path = os.path.join(f_path, os.pardir)
# sys.path.append(os.path.abspath(root_path))

# Import of the desired module
import src.compute_flask_cv.computer_vision as cvn


# pytest
def test_eye_unit8():
    sz = 2
    res_sz = cvn.eye_unit8(sz)
    assert (res_sz == [[1, 0], [0, 1]]).all()


def test_rgb2gray():
    current_wd = os.getcwd()
    cannon_path = os.path.join(current_wd, "src", "A_Cannone.jpg")
    cvn.rgb2gray(cannon_path)
    cvn.cv2.destroyAllWindows()
    assert os.path.exists(os.path.join(current_wd, "src", "A_Cannone_gray.jpg")) == 1


def test_rgb2bgr():
    current_wd = os.getcwd()
    cannon_path = os.path.join(current_wd, "src", "A_Cannone.jpg")
    cvn.rgb2gray(cannon_path)
    cvn.cv2.destroyAllWindows()
    assert os.path.exists(os.path.join(current_wd, "src", "A_Cannone_bgr.jpg")) == 1


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
    path = os.path.join(cwd, os.pardir, "src", "A_Cannone.jpg")
    match choice:
        case '1':
            gray, np_array_g = cvn.rgb2gray(path)
        case '2':
            bgr, np_array_b = cvn.rgb2bgr(path)
