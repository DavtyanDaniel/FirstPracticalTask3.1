import constants


class Stars:
    def __init__(self, ra, dec, star_id, mag):
        self.star_id = star_id
        self.ra = ra
        self.dec = dec
        self.mag = mag
        self.euclidean_distance = ((ra - constants.RA) ** 2 + (dec - constants.DEC) ** 2) ** 0.5

    def __repr__(self):
        return f"{self.star_id}, {self.ra}, {self.dec}, {self.mag}, {self.euclidean_distance}\n"

    def get_mag(self):
        return self.mag

    def get_distance(self):
        return self.euclidean_distance


