import base64
import sys
import pprint

import my_base64

words = ['hello', 'hello world', '123', 'Programming', '\n', "i don't like the sugar coat", "i'm a striiiiing!"]


def perform_tests():
    my_res = []
    py_res = []
    print('Words used for test: ')
    print(words)
    for word in words:
        my_res.append(my_base64.encode(word))
        py_res.append(base64.b64encode(bytes(word, encoding=sys.stdout.encoding)).decode(sys.stdout.encoding))
    print()
    print('My res: ')
    print(my_res)
    print()
    print('Py res: ')
    print(py_res)
    diff = list(set(py_res) - set(my_res))
    print()
    if len(diff) == 0:
        print('No difference found')
    else:
        print('Difference: ')
        pprint.pprint(diff)


def perform_self_test():
    words = ['1', 'Twitch.tv', 'py', 'pypi', 'Mister Solodushkin']
    encoded = []

    for word in words:
        encoded.append(my_base64.encode(word))

    decoded = []

    for word in encoded:
        decoded.append(my_base64.decode(word))

    print('Words used: ')
    print(words)
    print()
    print('Encode + decode res: ')
    print(decoded)
    print()
    diff = list(set(words) - set(decoded))
    if len(diff) == 0:
        print('No difference found')
    else:
        print('Difference: ')
        pprint.pprint(diff)
