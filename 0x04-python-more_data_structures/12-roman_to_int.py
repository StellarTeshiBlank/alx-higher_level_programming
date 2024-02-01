#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0
    last_rom = 0

    for ch in reversed(roman_string):
        value = rom_n.get(ch, 0)
        if value < last_rom:
            num -= value
        else:
            num += value
        last_rom = value

    return num
