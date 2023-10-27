import requests   #importing the requests library for fetching information through final URL

base_url = "https://api.openweathermap.org/data/2.5/weather?"  #base URL which contains the site info
api_key = open('api_key.txt', 'r').read()     #reading the text file that contains the api key to access the api

def temp_convert(kelvin):                     #function to convert temperature from kelvin to celsius and fahrenheit
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def try_again():                              #function to loop back to main menu in case the user wants to try other options
    print("Thank you for trying my python weather app!\nDo you wish to try again?")
    try_ans = input("Y/N: ").capitalize()
    if try_ans == "Y":
        main_menu()
    else:
        print("See you again!")

def main_menu():                              #main function that contains all the options and their responses
    print("Hello!\nWhat do you want to know about today's weather?\n")
    print("1) Temperature \n2) Humidity \n3) Windspeed \n4) Weather Description \n5) All of the above")
    menu_ans = int(input("Enter your choice: "))
    if menu_ans == 1:
        city = input("Enter a city: ").capitalize()
        URL = base_url + "appid=" + api_key + "&q=" + city  #this is the final url that will be used through the requests library
        response = requests.get(URL).json()
        
        temp_kelvin = response['main']['temp']              #accessing the temperature values through the dictionary method
        temp_celsius, temp_fahrenheit = temp_convert(temp_kelvin)

        print(f"Temperature in {city} in celsius : {temp_celsius:.2f}°C")
        print(f"Temperature in {city} in fahrenheit : {temp_fahrenheit:.2f}F")

        try_again()

    elif menu_ans == 2:
        city = input("Enter a city: ").capitalize()
        URL = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(URL).json()
        
        humidity = response['main']['humidity']             #accessing the humidity value through the dictionary method
        
        print(f"Humidity in {city} is : {humidity}%")

        try_again()

    elif menu_ans == 3:
        city = input("Enter a city: ").capitalize()
        URL = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(URL).json()

        wind_speed = response['wind']['speed']               #accessing the windspeed value through the dictionary method

        print(f"Wind speed in {city} is : {wind_speed}m/s ")

        try_again()

    elif menu_ans == 4:
        city = input("Enter a city: ").capitalize()
        URL = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(URL).json()
        
        description = response['weather'][0]['description']   #accessing the description value through the dictionary method

        print(f"Weather description for {city} is : {description}")

        try_again()

    elif menu_ans == 5:
        city = input("Enter a city: ").capitalize()
        URL = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(URL).json()
        
        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = temp_convert(temp_kelvin)
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']
        description = response['weather'][0]['description']

        print(f"Temperature in {city} in celsius : {temp_celsius:.2f}°C")
        print(f"Temperature in {city} in fahrenheit : {temp_fahrenheit:.2f}F")
        print(f"Humidity in {city} is : {humidity}%")
        print(f"Wind speed in {city} is : {wind_speed}m/s ")
        print(f"Weather description for {city} is : {description}")

        try_again()

    else:
        print("Please enter a valid choice!")
        try_again()

main_menu()                                                #calling the main fucntion
