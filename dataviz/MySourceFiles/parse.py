import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """
    Parse a raw file into a json lke object
    :param raw_file:
    :param delimiter:
    :return:
    """
    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV  file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list to collect data
    parsed_data = []

    # Skip over the first line for headers
    fields = csv_data.__next__()

    # Iterate over each row and create a dict of field along with its data
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the file
    opened_file.close()

    return parsed_data

# new_data = parse(MY_FILE, ",")
# print(new_data)

# def main():
#     # Call our parse function to read csv and create data
#     new_data = parse(MY_FILE, ',')
#     print(new_data)
#
#
# if __name__ == "__main__":
#     main()
