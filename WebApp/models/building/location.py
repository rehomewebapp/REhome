from geopy.geocoders import Nominatim
import csv
import os

data_path = "WebApp/models/building/data/"

def conv_zip_to_location(zip):
    """
    Convert postcode (zip) into information about the location.
    If no information can be found returns None.
    Otherwise dict with city, latitude and longitude will be returned.
    """
    geolocator = Nominatim(user_agent="rehome")
    loc = geolocator.geocode({"postalcode":zip})
    if loc == None:
        return loc
    city = loc[0].split(",")[0] # extract city from string
    lat = round(loc.latitude,2)
    long = round(loc.longitude,2)

    return {"city":city, "latitude":lat, "longitude":long}

def save_location_data(location):
    """
    save the location dictionary as csv file in the building models
    data directory.
    """
    city = location['city']
    lat = location['latitude']
    long = location['longitude']
    with open(data_path + "userid_location.csv", 'w') as csvfile:
        fieldnames = ['city','latitude','longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(location)

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