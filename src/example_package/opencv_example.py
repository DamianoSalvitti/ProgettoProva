import cv2, os
import numpy as np

def eye_unit8(s):
    eye = np.eye(s, dtype="uint8")
    return eye

def rgb2gray(path):
    # Read, convert
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Write
    new_path_idx = path.rfind("\\")
    new_path = path[0:new_path_idx]
    np_array = cv2.imwrite(new_path + "\\new_photo_gray.jpg", gray)

    # Show
    cv2.imshow("New - Gray", gray)
    print('\nPremere un tasto qualsiasi con la finestra "New - Gray" in primo piano.\n')
    cv2.waitKey(0)
    
    return gray, np_array

def rgb2bgr(path):
    # Read, convert
    img = cv2.imread(path)
    bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Write
    new_path_idx = path.rfind("\\")
    new_path = path[0:new_path_idx]
    np_array = cv2.imwrite(new_path + "\\new_photo_bgr.jpg", bgr)

    # Show
    cv2.imshow("New - BGR", bgr)
    print('Premere un tasto qualsiasi con la finestra "New - BGR" in primo piano.')
    cv2.waitKey(0)

    return bgr, np_array

if __name__ == '__main__':
    print('Stai eseguendo il file "opencv_example.py"!\n')

    cwd = os.getcwd()
    path = cwd + "\..\\" + "example_photo.jpg"

    # Matrix eye
    matrix = eye_unit8(3)
    print('Matrice identita\' di dimensione: 3')
    print(matrix)

    # rgb2gray
    gray, np_array_g = rgb2gray(path)

    # rgb2bgr
    bgr, np_array_b = rgb2bgr(path)

    # Close all windows
    cv2.destroyAllWindows()
