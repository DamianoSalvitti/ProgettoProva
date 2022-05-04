import sys, os
f_path = os.path.dirname(__file__)
parent_path = os.path.join(f_path, '..')
sys.path.append(os.path.abspath(parent_path))

from src.example_package.opencv_example import *

if __name__ == '__main__':
    print('Modulo "opencv_example" importato correttamente.')
    print('Avvio test del modulo "opencv_example.py"\n')

    size = int(input('Inserisci la dimensione della matrice da testare con "eye_unit8": '))

    res_size = eye_unit8(size)
    print(f'Matrice identita\' di dimensione: {size}')
    print(res_size)

    choice = input('Scegliere il numero per visualizzare e generare la conversione della foto:\n' +
                   '1: RGB -> Scala di grigi\n' +
                   '2: RGB -> BRG\n')

    cwd = os.getcwd()
    path = cwd + "\..\src\\" + "example_photo.jpg"
    match choice:
        case '1':
            gray, np_array_g = rgb2gray(path)
        case '2':
            bgr, np_array_b = rgb2bgr(path)
    cv2.destroyAllWindows()
