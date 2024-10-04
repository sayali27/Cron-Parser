import sys

from parser.parser import parse_expression

def main():
    args = sys.argv[1:]
    if len(args) > 1:
        raise ValueError("Sorry, please enter only one expression")
    parse_expression(args.pop())
    

if __name__ == '__main__':
    main()