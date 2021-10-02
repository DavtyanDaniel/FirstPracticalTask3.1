from datetime import datetime
from stars_filtering import filtering_by_coordinates, computing_range_of_square


def open_and_parse_file(file_name, fov_ra_min, fov_ra_max, fov_dec_min, fov_dec_max):
    """
        Function not only opening and parsing the file but also filtering them with the help
        of filtering_by_coordinates function.
    """
    try:
        with open(file_name, 'r') as tsv_file:
            list_of_objects = []

            for row in tsv_file:
                try:
                    splitted_row = row.split("\t")
                    data = filtering_by_coordinates(splitted_row, fov_ra_min, fov_ra_max, fov_dec_min, fov_dec_max)
                    if data is not None:
                        list_of_objects.append(data)
                except ValueError:
                    pass

    except FileNotFoundError:
        raise Exception(f'path isn\'t correct {file_name}')

    return list_of_objects


def write_the_file(filtered_stars: list):

    with open(f"{datetime.now()}.csv", 'w') as f:
        header = "RA, DEC, ID, Magnitude, Dis_from_gv_point\n"
        f.write(header)

        for star in filtered_stars:
            row_data = f'{star.star_id}' + ',' + \
                       f'{star.ra},' + \
                       f'{star.dec},' + \
                       f'{star.mag},' + \
                       f'{star.euclidean_distance} \n'
            f.write(row_data)


if __name__ == "__main__":
    range1 = computing_range_of_square(40, 50, 20, 30)
    print(open_and_parse_file("337.all.tsv", range1[0], range1[1], range1[2], range1[3]))

