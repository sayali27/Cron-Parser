import sys

from parser.parser import parse_expression

def main():
    print('in main')
    args = sys.argv[1:]
    if len(args) > 1:
        print("Throw an exception, more than one arg not supported")
        return 1
    parse_expression(args[0])
    

if __name__ == '__main__':
    main()