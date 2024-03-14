#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv[1:]) < 1:
        print("{} arguments.".format(0))
    elif len(argv[1:]) == 1:
        print("{} argument:".format(len(argv[1:])))
    else:
        print("{} arguments:".format(len(argv[1:])))

    for idx, arg in enumerate(argv[1:]):
        print("{:d}: {:s}".format(idx + 1, arg))
