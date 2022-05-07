import os
import cv2
import numpy as np

# Make matrix
def eye_unit8(s):
    eye = np.eye(s, dtype="uint8")
    return eye

# Convert from RGB to Gray scale
def rgb2gray(path):
    # Read, convert
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Write
    f_path = os.path.dirname(__file__)
    new_path = os.path.join(f_path,os.pardir,"A_Cannone_gray.jpg")
    np_array = cv2.imwrite(new_path, gray)

    # Show
    cv2.imshow("New - Gray", gray)
    print('\nPlease press any key on the "New - Gray" window.\n')
    cv2.waitKey(0)
    
    return gray, np_array

# Convert from RGB to BGR
def rgb2bgr(path):
    # Read, convert
    img = cv2.imread(path)
    bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Write
    f_path = os.path.dirname(__file__)
    new_path = os.path.join(f_path,os.pardir,"A_Cannone_bgr.jpg")
    np_array = cv2.imwrite(new_path, bgr)

    # Show
    cv2.imshow("New - BGR", bgr)
    print('\nPlease press any key on the "New - BGR" window.\n')
    cv2.waitKey(0)

    return bgr, np_array

if __name__ == '__main__':
    print('Running "computer_vision.py"!\n')

    # Matrix eye
    matrix = eye_unit8(3)
    print('Dimension of the identity matrix: 3')
    print(matrix)

    # Get photo's path
    cwd = os.getcwd()
    path = os.path.join(cwd,os.pardir,"A_Cannone.jpg")

    # Convert
    gray, np_array_g = rgb2gray(path)
    bgr, np_array_b = rgb2bgr(path)

    # Close all windows
    cv2.destroyAllWindows()
