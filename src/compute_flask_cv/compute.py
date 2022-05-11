def add_one(number):
    return number + 1


def x_times_y(x, y):
    return x*y


if __name__ == '__main__':
    print('Running "compute.py"!\n')
    print('Hereunder a list of number will be printed:\n')
    for i in range(1, 13, 2):
        print(add_one(i))
        print(x_times_y(i, i-2))
