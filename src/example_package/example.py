def add_one(number):
    return number + 1

def x_times_y (x, y):
    return x*y

if __name__ == '__main__':
    print('Stai eseguendo il file "example.py"!\n')
    print('Qui sotto viene stampata una lista di numeri:\n')
    for i in range(1,13,2):
        print(add_one(i))
        print(x_times_y(i,i-2))

