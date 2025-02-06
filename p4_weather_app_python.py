import requests

def get_weather(city):
    api_key = "your_api_key_here" 
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    