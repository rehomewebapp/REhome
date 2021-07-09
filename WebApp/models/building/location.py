from geopy.geocoders import Nominatim
import csv
import os

data_path = "WebApp/models/building/data/"



def read_location_data():
    """
    load the location data from a csv file.
    """
    with open(data_path + "userid_location.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            location = row
    return location


if __name__ == "__main__":
    location = conv_zip_to_location(79271)
    #print(location)
    #print(os.getcwd())
    #save_location_data(location)
    #location = read_location_data()
    #print(location)