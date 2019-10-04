#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program tells you if number is +, -, or 0

import random


def main():
    # funciton finds +, -, or 0 number

    # Welcome statement
    print("Welcome, this is the NUMBER thing with + and - and 0.")
    input("Press Enter to continue.")

    # input
    number = float(input("What is your number: "))

    # process
    if number < 0:
        print("-")
    elif number > 0:
        print("+")
    else:
        print("0")


if __name__ == "__main__":
    main()
