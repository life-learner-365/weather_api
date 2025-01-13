import requests
import json
import csv

#scrape page
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

#request page
page = requests.get(URL)

#convert object to json object
data = page.json()

#save json object file
save_file = open("data/json/forecast_data.json", "w") 
json.dump(data, save_file, indent = 6)  
save_file.close()

#load json file
with open("data/json/forecast_data.json") as f:
   data = json.load(f)
   f.close()

#modify json file to keep hourly data 
hourly_data = data["hourly"]

#indicate field names for csv file
field_names = ["Time", "Temperature (C)", "Relative Humidity (%)", "Precipitation (mm)", "Surface Pressure (hPa)"]

#write json object to csv file
with open("data/csv/final_weather_data.csv", "w") as csvfile: 
   writer = csv.writer(csvfile)
   
   #convert dicitonary keys to a list:
   headers = list(hourly_data.keys())

   #set field names for csv file
   writer.writerow(field_names)

   #iterate each column to assign corresponding values
   for i in range(len(hourly_data["time"])):
      writer.writerow(hourly_data[x][i] for x in headers)

   csvfile.close()
      



   

      


      







