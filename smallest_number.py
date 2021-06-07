#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: June 2021
# This program determines the smallest of 10 numbers


import random


def smallest_number(ten_numbers):

    smallest_int = ten_numbers[0]

    for loop_counter in range(0, len(ten_numbers)):
        if smallest_int <= ten_numbers[loop_counter]:
            continue
        elif smallest_int > ten_numbers[loop_counter]:
            smallest_int = ten_numbers[loop_counter]

    return smallest_int


def main():

    ten_numbers = []
    print("Here are 10 numbers:")

    for loop_counter in range(1, 10):
        random_numbers = random.randint(1, 100)
        ten_numbers.append(random_numbers)
        print(random_numbers)

    small_num = smallest_number(ten_numbers)

    print("The smallest number is {0}".format(small_num))


if __name__ == "__main__":
    main()
