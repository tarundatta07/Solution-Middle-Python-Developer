import requests

api_key = '5412dc01a36f405194e1ee19a306a885'


# ======= Function to geocode an address ====================
def geocode_address(address):
	base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
	params = {
		'address': address,
		'key': api_key,
	}

	try:

		response = requests.get(base_url, params=params)
		if response.status_code == 200:
			data = response.json()
			if data['status'] == 'OK':
				location = data['results'][0]['geometry']['location']
				lat = location['lat']
				lng = location['lng']
				return lat, lng
			else:
				print(f"Geocoding failed: {data['status']}")
				return None
		else:
			print(f"Request failed with status code {response.status_code}")
			return None

	except Exception as e:
		print(f"Error: {str(e)}")
		return None


address_to_geocode = "Ring Road, Mohammadpur, Dhaka"
coordinates = geocode_address(address_to_geocode)

if coordinates:
	print(f"Coordinates for {address_to_geocode}:")
	print(f"Latitude: {coordinates[0]}")
	print(f"Longitude: {coordinates[1]}")
else:
	print(f"Geocoding failed for {address_to_geocode}")
