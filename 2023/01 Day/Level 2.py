import numpy as np
import sys
import os

numwords = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
            'eight': 8, 'nine': 9}
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def replace_numwords(line: str):
    s = line
    for numword in numwords.keys():
        while numword in s:
            s = s.replace(numword, numword[0] + str(numwords[numword]) + numword[-1])
    return s


def find_calibration_number(line: str):
    line = replace_numwords(line)
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    for char in reversed(line):
        if char.isdigit():
            second_digit = char
            break
    calibration_number = int(first_digit + second_digit)
    # print(f"{line}: {calibration_number}")
    return calibration_number


with open(os.getcwd() + "\\Puzzle Input.txt", "r") as f:
    calibration_numbers = []
    for line in f:
        calibration_numbers.append(find_calibration_number(line[:-1]))

calibration_numbers = np.array(calibration_numbers)
print(calibration_numbers.sum())
