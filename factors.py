#!/usr/bin/env python3
import sys

def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return (i, number // i)
    return (number, 1)

def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            print(f"{number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    main(input_file)
