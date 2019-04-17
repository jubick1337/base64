import sys

import utils


def encode(source):
    binary_input = ' '.join(map(bin, bytearray(source, sys.stdout.encoding))).replace('b', '').split(' ')
    binary_input = ''.join(utils.fix_binary(binary_input))
    binary_input = [binary_input[i:i + 6] for i in range(0, len(binary_input), 6)]
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    res = ''
    init_len = len(''.join(binary_input))

    while len(binary_input[len(binary_input) - 1]) != 6:
        binary_input[len(binary_input) - 1] += '0'

    for i in range(len(binary_input)):
        res += table[int(binary_input[i], 2)]

    if init_len % 3 == 1:
        res += '='
    elif init_len % 3 == 2:
        res += '=='
    return res


def decode(source):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    ints = []

    eq_count = len(list(filter(lambda x: x == '=', source)))

    source = source.replace('=', '')
    for letter in source:
        ints.append(table.index(letter))

    bits = []

    for n in ints:
        bits.append(format(n, '06b'))

    bits = ''.join(bits)
    if eq_count != 0:
        bits = bits[:-eq_count * 2]
    bytes_of_str = [bits[i:i + 8] for i in range(0, len(bits), 8)]

    res = ''

    for i in range(0, len(bytes_of_str)):
        res += chr(int(bytes_of_str[i][:8], 2))

    return res
