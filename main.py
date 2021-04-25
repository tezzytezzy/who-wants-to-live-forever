
def main():
    read_file("1.in")

def read_file(data_file):
    with open (data_file, 'rt', encoding="ISO-8859-1") as input_file:
        line_counter = 1
        for a_line in input_file:
            # Skip the first line as it contains the number of data, not actual data
            if line_counter != 1:
                test_live_or_die(a_line)

            line_counter += 1

def test_live_or_die(a_line: str):
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

def recursive_live_pattern(old_str: str) -> bool:
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
    
    # '11' is so unique that it repeats itself forever
    return new_str, \
            True if ((pos_products == 1) or old_str == '11') else False

def get_new_str(test_str: str) -> str:
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