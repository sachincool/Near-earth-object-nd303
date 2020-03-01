from enum import Enum
import csv


class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """

    display = "display"
    csv_file = "csv_file"

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported output formatting options.
    """

    def __init__(self):
        # TODO: How can we use the OutputFormat in the NEOWriter?
        self.output_formats = OutputFormat.list()

    def to_csv(self, data):
        """
        Function to print results to a csv file

        :param data: collection of NearEarthObject or OrbitPath results
        output: results.csv file
        """
        with open("results.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "name", "diameter_min_km", "orbits", "orbit_dates"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for neo_object in data:
                writer.writerow(
                    {
                        "id": neo_object.id,
                        "name": neo_object.name,
                        "diameter_min_km": neo_object.diameter_min_km,
                        "orbits": [orbit.neo_name for orbit in neo_object.orbits],
                        "orbit_dates": [
                            orbit.close_approach_date for orbit in neo_object.orbits
                        ],
                    }
                )

        # TODO: Using the OutputFormat, how can we organize our 'write' logic for output to stdout vs to csvfile
        # TODO: into instance methods for NEOWriter? Write instance methods that write() can call to do the necessary
        # TODO: output format.

    def write(self, format, data, **kwargs):
        """
    Generic write interface that, depending on the OutputFormat selected calls the
    appropriate instance write function

    :param format: str representing the OutputFormat
    :param data: collection of NearEarthObject or OrbitPath results
    :param kwargs: Additional attributes used for formatting output e.g. filename
    :return: bool representing if write successful or not
    """

        # TODO: Using the OutputFormat, how can we organize our 'write' logic for output to stdout vs to csvfile
        # TODO: into instance methods for NEOWriter? Write instance methods that write() can call to do the necessary
        # TODO: output format.
        if format == self.output_formats[0]:
            try:
                self.stdout(data)
                return True
            except IOError as e:
                return False

        elif format == self.output_formats[1]:
            try:
                self.to_csv(data)
                return True
            except IOError as e:
                return False

        else:
            return False
