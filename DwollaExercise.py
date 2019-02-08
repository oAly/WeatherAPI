import requests

name = input("\nWhere are you? ")
print(name.split(' ')[0], "weather:")

parameters = {"q": name.split(' ')[0], "appid": "75a95590d938a1146075143183267dc9"}

# Make a get request to grab the weather to user input city
response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parameters)

# Print the status code of the response.
if response.status_code < 400: # GET is successful
    data = response.json() # get the response of the API call
    temp = data['main']['temp'] - 273 # convert temp from K to C
    temp_F = temp * 9/5 + 32 # convert to F
    print(round(temp_F), "degrees Fahrenheit\n")
