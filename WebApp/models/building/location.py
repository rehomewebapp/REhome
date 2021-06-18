from geopy.geocoders import Nominatim

def conv_zip_to_location(zip):
    '''
    Convert postcode (zip) into information about the location.
    If no information can be found returns None.
    Otherwise dict with city, latitude and longitude will be returned.
    '''
    geolocator = Nominatim(user_agent="rehome")
    loc = geolocator.geocode({"postalcode":zip})
    if loc == None:
        return loc
    city = loc[0].split(",")[0] # extract city from string
    lat = round(loc.latitude,2)
    long = round(loc.longitude,2)

    return {"city":city, "latitude":lat, "longitude":long}


if __name__ == "__main__":
    loc = conv_zip_to_location(79271)
    print(loc)