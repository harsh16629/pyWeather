# PyWeather

## Project Description

PyWeather is a web-based platform that allows users to search for weather information in various cities. Users can view detailed weather data, leave comments about the weather, and manage their profiles, including viewing their search history and comments.

## Key Features

- **User Authentication**: Secure login and registration for users.
- **Weather Search**: Users can search for the weather in any city.
- **Detailed Weather Information**: Displays temperature, humidity, wind speed, and visibility for the searched city.
- **Comments Section**: Users can leave comments about the weather, which are stored and displayed.
- **User Profile**: Users can view their username, search history, and comments made on the platform.

## Installation Instructions

To set up the Weather Application locally, follow these steps:

1. **Clone the Repository**:
   ``'bash
   git clone https://github.com/yourusername/weather-application.git
   cd weather-application
2. **Create a Virtual Environment (optional)**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Requirements:**
   pip install -r requirements.txt
4. **Run Migrations:**  
   python manage.py migrate
5. **Create a Superuser (to access the admin panel):**  
   python manage.py createsuperuser
6. **Run the Development Server:** 
   python manage.py runserver
7. **Open Your Browser: Go to http://127.0.0.1:8000 to view the application.**

Usage Examples
Search Weather: Navigate to the home page and enter a city name to fetch the weather details.
Post Comments: After retrieving weather information, you can leave comments about your thoughts or experiences regarding the weather.
View Profile: Users can check their profile to view their search history and comments.
API Endpoints
1. **Get Weather Data**
Endpoint: GET /api/weather/{city}
Description: Fetches weather data for a specified city.
Request Parameters:
city: Name of the city to get weather information for.
Response Format:
{
  "city": "City Name",
  "temperature": "Value in °C",
  "humidity": "Value in %",
  "wind_speed": "Value in km/h",
  "visibility": "Value in km",
  "pressure": "Value in hPa",
  "weather_description": "Description of the weather",
  "min_temp": "Min temperature",
  "max_temp": "Max temperature"
}
2. **Post Comment**
Endpoint: POST /api/comments/
Description: Allows a user to post a comment about the weather.
Request Body:
{
  "comment": "Your comment text here"
}
Response Format:
{
  "message": "Comment added successfully."
}
**Authentication Requirements**
Users must be authenticated to post comments.
Use the login credentials to access the comment functionality.
Registration is required for new users.
**License**
This project is licensed under the MIT License. See the LICENSE file for more details.
**Contributing**
Contributions are welcome! Please create a pull request or open an issue to discuss your ideas.

**Acknowledgments**
Django for the web framework.
Bootstrap for the front-end framework.
OpenWeatherMap for weather data API.

   
