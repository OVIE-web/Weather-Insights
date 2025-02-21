import tkinter as tk
import tkinter.messagebox as messagebox
import requests
import threading
import time

# Function to get weather data
def get_weather(city_name, api_key):
  try:
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    if data["cod"] != 200:
      return None, data["message"] #return error message
    return data, None
  except requests.exceptions.RequestException as e:
    messagebox.showerror("Error", f"Failed to fetch weather data: {e}")
    return None, str(e)

# Function to show weather notification
def show_weather():
  city_name = city_entry.get()
  api_key = "eb9fb5b5cd49a8c5ac2f493f74b60e07"  # OpenWeatherMap API key

  if not city_name:
    messagebox.showwarning("Warning", "Please enter a city name.")
    return

  weather_data, error = get_weather(city_name, api_key)

  if error:
    messagebox.showerror("Error", error)
    return

  if weather_data:
    main = weather_data["main"]
    temp = main["temp"]
    humidity = main["humidity"]
    pressure = main["pressure"]
    weather_desc = weather_data["weather"][0]["description"]
    weather_info = f"City: {city_name}\nTemperature: {temp}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_desc}"
    messagebox.showinfo("Weather Information", weather_info)
  else:
      messagebox.showerror("Error", "City Not Found or API error")


# Create the main window
root = tk.Tk()
root.title("Live Weather Notifications")
root.geometry("400x200")

# Add widgets to the window
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

notify_button = tk.Button(root, text="Get Weather", command=show_weather)
notify_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
