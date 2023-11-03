#!/usr/bin/python3

# Entry point for the script
if __name__ == '__main__':
    import add_0 as add
    a = 1
    b = 2

    x = add.add(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, x))
