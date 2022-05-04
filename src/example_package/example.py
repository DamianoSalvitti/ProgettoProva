def add_one(number):
    return number + 1

if __name__ == '__main__':
    print('"Hello from example" come main!\n')
    print('Qui sotto viene stampata una lista di numeri:\n')
    for i in range(1,13,2):
        print(add_one(i))

