from geopy.geocoders import Nominatim
geolocator = Nominatim()

address = "manchester"
location = geolocator.geocode(address)

print(location.latitude, location.longitude)