import sys, os
f_path = os.path.dirname(__file__)
parent_path = os.path.join(f_path, '..')
sys.path.append(os.path.abspath(parent_path))

from src.example_package.example import *

if __name__ == '__main__':
    print('Modulo "example" importato correttamente.')
    print('Avvio test del modulo "example.py"\n')
    
    add = float(input('                Inserisci il numero da testare con "add_one": '))
    res_add = add_one(add)

    times = input('Inserisci i due numeri ("n1, n2") da testare con "x_times_y": ')
    times = times.split(sep=',')
    times0 = float(times[0])
    times1 = float(times[1])
    res_times = x_times_y(times0,times1)

    print(f'\nAggiungere 1 a {add} -> {res_add}')
    print(f'Moltiplicare {times0} e {times1} -> {res_times}')
