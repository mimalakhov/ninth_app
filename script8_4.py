import logging
import time

''' Написать функцию. Для неё написать декораторы для следующего функционала:
    ◦ логирование выполнения функции;
    ◦ время выполнения функции;
    ◦ замедлить выполнение кода. Ограничить частоту вызова функции.
'''

#Функции для декорирования_______________________________________________________________________-
def div():
    print(int(input())/int(input()))

def long_func():
    for i in range(10):
        a = 1000000000000000000000000000*10000000000000
        b = 1000000000000000*100000000000000
        c = 1.23456*2.3456789

def print_num():
    print(int(input()))
    print()
    print(int(input()))

#Декораторы________________________________________________________________________
def decorator_for_div(func):
    def wrapper():
        logging.info("Program started!")
        try:
            func()
        except ZeroDivisionError:
            logging.error("Something bad!!!")
        logging.info("Program end!")
    return wrapper

def decorator_for_long_func(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Time: {end-start}')
    return wrapper

def decorator_for_print_num(func):
    def wrapper():
        func()
        time.sleep(1)
    return wrapper

#Работа декораторов_________________________________________________________________
div_new = decorator_for_div(div)
div_new()

long_new = decorator_for_long_func(long_func)
long_new()

print_new = decorator_for_print_num(print_num)
time_new = time.time()
while True:
    print("Start function? 1/0")
    answer = int(input())
    if(answer==0):
        break
    elif(answer==1):
        print("Start")
        if (time.time() - time_new >= 10): 
            print_new()
        else:
            print("Not yet!")
        time_new = time.time()
        print("End")
    else: 
        break
