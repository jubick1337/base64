import sys

import my_base64
import tests


def main():
    if len(sys.argv) < 2:
        print('usage: b64 [keys] [string]')
        print('-e   encode string from [string]')
        print('-d   decode string from [string]')
        print('-t   test preloaded tests')
        print('-st  performs enc + dec self test')
        print()
        print('Author Matvey Novikov')
        return

    key = sys.argv[1:2][0]
    arg = ' '.join(sys.argv[2:])

    if key == '-e':
        if len(arg) == 0:
            raise ValueError('Arguments error')
        else:
            print('Encoded: ')
            print(my_base64.encode(arg))

    elif key == '-d':
        if len(arg) == 0:
            raise ValueError('Arguments error')
        else:
            print('Decoded: ')
            print(my_base64.decode(arg))

    elif key == '-t':
        tests.perform_tests()

    elif key == '-st':
        tests.perform_self_test()


if __name__ == "__main__":
    main()
