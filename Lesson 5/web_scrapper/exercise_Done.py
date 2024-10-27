#Scraping Data from a JSON API Source, Storing it in a CSV File, and Sorting by Columns

#Objective:

#Create a Python script using requests to retrieve data from a JSON API (e.g., weather data from Open-Meteo), store it in a CSV file, and sort the data by a specific column (e.g., temperature or wind speed).

#Pseudo Code:

#	1.	Send a Request to the API:
#	•	Use the requests library to send a GET request to the API.
#	2.	Check for a Successful Response:
#	•	Verify that the response’s status code is 200 (OK).
#	3.	Parse the JSON Data:
#	•	Convert the JSON response into a Python dictionary.
#	4.	Extract and Organize Data:
#	•	Extract relevant fields (e.g., temperature, humidity, wind speed) and organize them into a list of dictionaries for easier handling.
#	5.	Store Data in a CSV File:
#	•	Write the extracted data into a CSV file with appropriate headers (e.g., temperature, humidity, wind_speed).
#	6.	Sort Data by a Specific Column:
#	•	Sort the CSV data by a user-specified column (e.g., by temperature or wind_speed) before writing to the file.

# import requests
# import csv
# import operator

# # API URL for weather data (Berlin, for example)
# api_url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

# # Send request to the Open-Meteo API
# response = requests.get(api_url)

# # Check for successful response
# if response.status_code == 200:
#     data = response.json()

# print(data)



# --------------------------------------------> Soltion Code : <--------------------------------------------

import requests
import csv
import operator

# API URL for weather data (Berlin, for example)
api_url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

# Send request to the Open-Meteo API
response = requests.get(api_url)

# Check for successful response
if response.status_code == 200:
    data = response.json()

    # Extract relevant fields: temperature, humidity, and wind speed
    hourly_data = data['hourly']
    temperature = hourly_data['temperature_2m']
    humidity = hourly_data['relative_humidity_2m']
    wind_speed = hourly_data['wind_speed_10m']
    timestamps = hourly_data['time']

    # Combine the extracted data into a list of dictionaries
    weather_data = []
    for i in range(len(timestamps)):
        weather_data.append({
            'timestamp': timestamps[i],
            'temperature': temperature[i],
            'humidity': humidity[i],
            'wind_speed': wind_speed[i]
        })

    # Specify the filename for the CSV file
    csv_filename = 'weather_data.csv'

    # Define the CSV headers
    headers = ['timestamp', 'temperature', 'humidity', 'wind_speed']

    # Write the data into a CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(weather_data)

    print(f"Data successfully written to {csv_filename}")

    # Prompt user for sorting column
    sort_column = input("Enter the column to sort by (temperature, humidity, wind_speed): ")

    # Sort the weather data by the user-specified column
    weather_data_sorted = sorted(weather_data, key=operator.itemgetter(sort_column))

    # Write the sorted data into a new CSV file
    sorted_csv_filename = f'sorted_weather_data_by_{sort_column}.csv'
    with open(sorted_csv_filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(weather_data_sorted)

    print(f"Sorted data successfully written to {sorted_csv_filename}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
