import mysql.connector
import requests

def apiing(longitude,latitude):
    print("entered into api")
# Replace 'YOUR_API_KEY' with the actual API key you created in the Google Cloud Console.
    api_key = 'AIzaSyAAJdC4F21cRQ1dA44GLMdhSfVG4BSZzLM'

# Define the base URL for the Places API
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

# Define your search query
    query = f'hospital'

# Create the full URL with the query and API key
    url = f'{base_url}query={query}&key={api_key}'

# Make the API request
    response = requests.get(url)
    data = response.json()

# Process the API response
    if 'results' in data:
        for place in data['results']:
            return (place['name'])
    else:
        return "Sorry but some error is thier"




mydb = mysql.connector.connect(host="localhost", user="root", passwd="nopassword")
mycursor = mydb.cursor()
mycursor.execute("USE medihelp")

def authentication(user_name, password):
    mycursor.execute("SELECT password FROM authenticator WHERE user_name = %s", (user_name,))
    data = mycursor.fetchall()
    if data and password == data[0][0]:
        return True
    else:
        return False

def appointment(name, age, cause, doctor):
    mycursor.execute("SELECT bookings FROM doctors WHERE doctorname = %s", (doctor,))
    data = mycursor.fetchall()
    
    if len(data) == 0:
        return "Sorry, today's appointments are full"
    else:
        data = int(data[0][0])  # Convert to integer
        print(name, age, cause, doctor)
        insert_query = f"INSERT INTO {doctor} (name, age, caluse, doctor) VALUES (%s, %s, %s, %s)"
        insert_data = (name, age, cause, doctor)
        mycursor.execute(insert_query, insert_data)
        mycursor.execute("UPDATE doctors SET bookings = %s WHERE doctorname = %s", (str(data - 1), doctor))
        mydb.commit()  # Make sure to commit changes
        return f"Your appointment is booked at number {100 - data}"
