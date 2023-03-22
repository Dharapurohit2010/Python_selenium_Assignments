import math


def volume_of_sphere(r):
    volume_s = 3.14 * r * r * r * 4 / 3
    return volume_s


def volume_of_cylinder(r, h):
    volume_c = 3.14 * r * r * h
    return volume_c


def volume_of_cone(r, h):
    volume_co = (3.14 * r * r * h) / 3
    return volume_co


def volume_of_cuboid(l, b, h):
    volume_cu = l * b * h
    return volume_cu
