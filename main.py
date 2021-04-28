# Google Python Style Guide
# https://google.github.io/styleguide/pyguide.html

# Per PEP 484, type notation adds type "hints" to variables, to inform what the type of a variable should be.
# These hints are ignored by the interpreter and are used solely to increase the readability.
# It does neither affect or be enforced by the runtime of the program in any way.
# 
# For multiple return type annotation, use "Tuple" as below
from typing import Tuple


def main():
    read_file("1.in")

def read_file(data_file: str):
    """Reads input file.

    Args:
      data_file: The name of a file that contains test number(s) per line.

    Returns:
      N/A.
    """    
    with open (data_file, 'rt', encoding="ISO-8859-1") as input_file:
        line_counter = 1
        for a_line in input_file:
            # Skip the first line as it contains the number of data, not actual data
            if line_counter != 1:
                test_live_or_die(a_line)

            line_counter += 1

def test_live_or_die(a_line: str):
    """Prints "DIES" when a number changes to all zero(s), otherwise "LIVES"

    Args:
      a_line: A number - with carriage return ('\n').

    Returns:
      N/A.
    """
    # Remove carriage return at the end of line
    test_str = a_line [:len(a_line)-1]

    while True:
        if test_str == '0' * len(test_str):
            print("DIES")
            break

        new_str, recursive_flag = recursive_live_pattern(test_str)

        if recursive_flag or test_str == new_str:
            print("LIVES")
            break
        else:
            test_str = new_str

def recursive_live_pattern(old_str: str) -> Tuple[str, bool]:
    """Converts a string and checks if it's recursive.

    Args:
      old_str: A string to be converted.

    Returns:
      1. A converted string, and
      2. True if every digit of the number gets alternated between zero and one at every turn, otherwise False
    """
    pos_products = 1

    new_str = get_new_str(old_str)
    
    # old_str: 101010
    # new_str: 010101
    #          ------
    #          111111 (by adding the same position of the two strings)
    # pos_product = 1 * 1 * 1 * 1 * 1 * 1 = 1
    #
    # old_str: 100110
    # new_str: 010101
    #          ------
    #          110211
    # pos_product = 1 * 1 * 0 * 2 * 1 * 1 = 0
    for str_pos in range(len(old_str)):
        pos_products *= (int(old_str[str_pos]) + int(new_str[str_pos]))
    
    # A string such as '11' is so unique that it repeats itself forever
    # Thus, (old_str == new_str) examines such a scenario
    return new_str, \
            True if ((pos_products == 1) or (old_str == new_str)) else False

def get_new_str(test_str: str) -> str:
    """Converts a string.

    Args:
      test_str: A string to be converted.

    Returns:
      A converted string.
    """
    new_str = ''
    str_len = len(test_str)

    for char_pos in range(str_len):
        if char_pos == 0: 
            # Check the second character from left
            new_char = '1' if test_str[1] == '1' else '0'
        elif char_pos == (str_len - 1):
            # Check the second character from right
            new_char = '1' if test_str[str_len - 2] == '1' else '0'
        else:
            if (test_str[char_pos - 1] == '0' and test_str[char_pos + 1] == '1') or \
                (test_str[char_pos - 1] == '1' and test_str[char_pos + 1] == '0'):
                new_char = '1'
            else:
                new_char = '0'

        new_str += new_char

    return new_str

if __name__ == '__main__':
    main()