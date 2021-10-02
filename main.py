import parser
import stars_filtering
import constants


def main(file_path_or_name: str,
         ra: float,
         dec: float,
         fov_h: float,
         fov_v: float,
         number_of_stars: int):
    """
    This is main function, that units all the work in different functions.
    """

    range_of_square = stars_filtering.computing_range_of_square(ra, dec, fov_h, fov_v)
    filtered_stars = parser.open_and_parse_file(file_path_or_name,
                                                range_of_square[0],
                                                range_of_square[1],
                                                range_of_square[2],
                                                range_of_square[3])

    filtered_stars = stars_filtering.quicksort(filtered_stars, stars_filtering.get_mag, False)
    filtered_stars = stars_filtering.mag_slicing(filtered_stars, number_of_stars)
    filtered_stars = stars_filtering.quicksort(filtered_stars, stars_filtering.get_dis, True)
    parser.write_the_file(filtered_stars)

    for i in filtered_stars:
        print(i)


if __name__ == "__main__":
    main(constants.FILE_NAME, constants.RA, constants.DEC, constants.FOV_H, constants.FOV_V, constants.N)

