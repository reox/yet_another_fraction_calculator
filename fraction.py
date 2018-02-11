#!/usr/bin/env python3
from argparse import ArgumentParser
from math import floor
from fractions import gcd


def get_fraction(r, max_denom=128.0):
    """
    Return the nearest fraction for r.

    The maximum demoninator can be controlled via max_denom
    """

    rat = r - floor(r)

    for i in range(1, int(max_denom)):
        if i / max_denom > rat:
            break

    if abs(rat - (i / max_denom)) > abs(rat - ((i - 1)) / max_denom):
        i = i - 1

    g = gcd(i, max_denom)

    return floor(r), int(i / g), int(max_denom / g)


def main():
    p = ArgumentParser()

    p.add_argument("real", nargs="+", help="Return the nearest fraction for the real number")

    args = p.parse_args()

    for r in args.real:
        r = float(r)
        w, f1, f2 = get_fraction(r)

        print("{} --> {} {}/{}, Error {}".format(r, w, f1, f2, r - (w + f1/float(f2))))


if __name__ == "__main__":
    main()
