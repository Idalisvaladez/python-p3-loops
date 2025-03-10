#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i in range(10, 0, -1):
        print(i)
        i -= 1

    print("Happy New Year!")

def square_integers(int_list):
   return [integer ** 2 for integer in int_list]

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
