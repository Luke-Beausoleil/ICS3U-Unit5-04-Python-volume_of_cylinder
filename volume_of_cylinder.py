#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# this program calculates the volume of a cylinder

import math


def volume_of_cylinder(radius, height):
    # this function calculates the volume of a cylinder
    volume = math.pi * height * radius ** 2

    return volume


def main():
    # this function receives input and calls another function
    # input
    radius_as_string = input("Enter the radius (cm): ")
    height_as_string = input("Enter the height (cm): ")
    try:
        radius = int(radius_as_string)
        height = int(height_as_string)
        # check for integers & call function
        radius_as_float = float(radius_as_string)
        height_as_float = float(height_as_string)
        if radius != radius_as_float or height != height_as_float:
            print("Invalid. Enter positive integers only\nDone.")
        elif radius < 0 or height < 0:
            print("Invalid. Enter positive integers only\nDone.")
        else:
            print("The volume is {0}cm³\nDone.".format(
                  round(volume_of_cylinder(radius, height), 4)))
            # https://www.kite.com/python/answers/how-to-limit-a-float-to-two-
            #     decimal-places-in-python#:~:text=Call%20str.,decimal%20place
            #     s%20as%20a%20string.
    except (Exception):
        print("Invalid. Enter positive integers only\nDone.")


if __name__ == "__main__":
    main()
