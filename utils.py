def add_zeroes(string):
    while len(string) < 8:
        string = '0' + string[0:]
    return string


def fix_binary(bin_list):
    for i in range(len(bin_list)):
        bin_list[i] = add_zeroes(bin_list[i])
    return bin_list
