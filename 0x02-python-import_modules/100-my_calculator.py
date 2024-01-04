#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    try:
        if sys.argv[1] == "" or len(sys.argv) != 4:
            pass
    except IndexError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        val1 = int(sys.argv[1])
        val2 = int(sys.argv[3])
        if sys.argv[2] == '+':
            print(f"{val1} + {val2} = {add(val1, val2)}")
            sys.exit(0)
        elif sys.argv[2] == '-':
            print(f"{val1} - {val2} = {sub(val1, val2)}")
            sys.exit(0)
        elif sys.argv[2] == '*':
            print(f"{val1} * {val2} = {mul(val1, val2)}")
            sys.exit(0)
        elif sys.argv[2] == '/':
            print(f"{val1} / {val2} = {div(val1, val2)}")
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
