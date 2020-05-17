from parse import parse
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = '../data/sample_sfpd_incident_all.csv'


def visualize_data():
    # Get parsed data
    data_file = parse(MY_FILE, ',')

    # Create Counter to get no of incidents per day of week data
    counter = Counter(item['DayOfWeek'] for item in data_file)
    print(counter)

    # Create sorted list of days of week
    data_list = [counter['Monday'], counter['Tuesday'], counter['Wednesday'], counter['Thursday'],
                 counter['Friday'], counter['Saturday'], counter['Sunday']]

    # Create labels for x-axis
    day_tuple = tuple(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    # Plt the data
    plt.plot(data_list)

    # Add labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save figure
    plt.savefig('Days.png')

    # Close figure
    plt.clf()


def main():
    visualize_data()

if __name__ == "__main__":
    main()