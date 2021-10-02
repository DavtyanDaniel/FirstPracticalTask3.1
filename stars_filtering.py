from random import randint

import parser
from stars import Stars
import constants


def computing_range_of_square(ra, dec, fov_h, fov_v) -> tuple:
    """
    calculating the range of given FOV
    """
    # square's weight left number
    square_w_l = ra - fov_h / 2
    # square's weight right number
    square_w_r = ra + fov_h / 2
    # square's height left number
    square_h_l = dec - fov_v / 2
    # square's height right number
    square_h_r = dec + fov_v / 2

    return square_w_l, square_w_r, square_h_l, square_h_r


def filtering_by_coordinates(row: list,
                             square_w_l: float,
                             square_w_r: float,
                             square_h_l: float,
                             square_h_r: float) -> Stars:
    """
    filtering by ra/dec coordinates, for that we have to know the range of FOV, that's
    why in parameters list we have range of it.
    """
    # included_cols = [5, 6, 7, 22]   The columns that we needed(ra, dec, id, mag)
    if (square_w_l <= float(row[0]) <= square_w_r) and (square_h_l <= float(row[1]) <= square_h_r):

        return Stars(float(row[constants.RA_INDEX]),
                     float(row[constants.DEC_INDEX]),
                     int(row[constants.ID_INDEX]),
                     float(row[constants.MAG_INDEX]))


def checking_number_of_stars(filtered_stars: list, number_of_stars) -> int:
    """
    checking if given number of stars bigger than filtered stars
    """
    if len(filtered_stars) < number_of_stars:
        number_of_stars = len(filtered_stars)

    return int(number_of_stars)


def quicksort(list_of_objects: list, getter, reverse: bool) -> list:
        """
        a quicksort sorting algorithm that takes an array, getter function, and sort direction and returns a sorted array
        """

        if len(list_of_objects) < 2:
            return list_of_objects
        left = []
        same = []
        right = []
        delimiter = getter(list_of_objects[randint(0, len(list_of_objects) - 1)])

        for item in list_of_objects:
            value = getter(item)
            if value > delimiter:
                if reverse is False:
                    left.append(item)
                else:
                    right.append(item)
            elif value == delimiter:
                same.append(item)
            elif value < delimiter:
                if reverse is False:
                    right.append(item)
                else:
                    left.append(item)
        sorted_array = quicksort(left, getter, reverse) + same + quicksort(right, getter, reverse)

        return sorted_array


def get_mag(item):
    return item.mag


def get_dis(item):
    return item.euclidean_distance


def mag_slicing(ls: list, n: int) -> list:
    return ls[:n]


if __name__ == "__main__":
    range1 = computing_range_of_square(40, 50, 20, 30)
    print(quicksort(parser.open_and_parse_file('337.all.tsv', range1[0], range1[1], range1[2], range1[3]), get_mag, True))

