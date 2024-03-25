import numpy as np
import sys
import os

with open(os.getcwd() + "\\Puzzle Input.txt", "r") as f:
    calibration_numbers = []
    for line in f:
        for char in line[:-1]:
            if char.isdigit():
                first_digit = char
                break
        for char in reversed(line[:-1]):
            if char.isdigit():
                second_digit = char
                break
        calibration_numbers.append(int(first_digit + second_digit))
calibration_numbers = np.array(calibration_numbers)
print(calibration_numbers.sum())
