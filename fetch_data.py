import requests
import json

def fetch_flight_data():
    # Define the API endpoint and your access key
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        'access_key': 'c79af6b9b8a2d297e1d56d87be267605',
        'limit': 5  # Limits the results to 5 flights for easier reading
    }

    try:
        # Make the request to the API
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Print the data to the terminal
            print("Successfully fetched flight data:")
            print(json.dumps(data, indent=4))
            
            # Save the response to a .json file
            with open("flights_data.json", "w") as file:
                json.dump(data, file, indent=4)
            print("\nData has been saved to flights_data.json")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    fetch_flight_data()