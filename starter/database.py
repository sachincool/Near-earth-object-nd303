from models import OrbitPath, NearEarthObject
import csv


class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """
        # TODO: What data structures will be needed to store the NearEarthObjects and OrbitPaths?
        # TODO: Add relevant instance variables for this.
        self.filename = filename
        self.NearEarthObjects = dict()
        self.neo_name_map = {}

    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject

        :param filename:
        :return:
        """

        if not (filename or self.filename):
            raise Exception("Cannot load data, no filename provided")

        filename = filename or self.filename        # TODO: Load data from csv file.
        with open(filename, "r") as f:
            csvfile = csv.DictReader(f, delimiter=",")
            for row in csvfile:
                orbit_path = OrbitPath(**row)
                near_earth_object = NearEarthObject(**row)
                near_earth_object.update_orbits(orbit_path)

                if not self.neo_name_map.get(row["name"], None):
                    self.neo_name_map[row["name"]] = near_earth_object

                if row["close_approach_date"] in self.NearEarthObjects:
                    self.NearEarthObjects[row["close_approach_date"]].append(
                        near_earth_object
                    )

                else:
                    self.NearEarthObjects[row["close_approach_date"]] = [
                        near_earth_object
                    ]

        return None
