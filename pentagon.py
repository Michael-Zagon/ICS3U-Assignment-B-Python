#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program calculates the perimeter of a regular pentagon


def main():
    # This function calculates the perimeter of a regular pentagon

    # input
    length = int(input("Enter length of the regular pentagon (cm): "))

    # process
    perimeter = 5 * (length)

    # output
    print("")
    print("Perimeter is {0} cm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
