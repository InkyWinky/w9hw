import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Function to get latitude and longitude
def get_lat_long(city_name):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city_name)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

# Function to add latitude and longitude columns
def add_lat_long_to_csv(input_csv, output_csv):
    # Load the CSV file
    df = pd.read_csv(input_csv)
    KEY = "Location"
    # Check if the "location" column exists
    if KEY not in df.columns:
        raise ValueError('The input CSV file must contain a ' + KEY + ' column.')
    
    # Create empty lists to store latitude and longitude
    latitudes = []
    longitudes = []
    
    # Iterate through the cities in the "location" column
    for city in df[KEY]:
        latitude, longitude = get_lat_long(city)
        latitudes.append(latitude)
        longitudes.append(longitude)
    
    # Add the new columns to the DataFrame
    df['latitude'] = latitudes
    df['longitude'] = longitudes
    
    # Save the updated DataFrame back to a new CSV file
    df.to_csv(output_csv, index=False)
    print(f"Updated CSV file saved as {output_csv}")

# Example usage:
input_csv = 'Airplane_Crashes_and_Fatalities_Since_1908.csv'  # Input CSV file path
output_csv = 'updated_with_long_lat.csv'  # Output CSV file path

add_lat_long_to_csv(input_csv, output_csv)