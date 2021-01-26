import grovepi
import math
import time
from grove_rgb_lcd import *
# Need to import json library
import json

# Connect Grove Temperature & Humidity Sensor Pro to digital port D5
sensor = 7

# temp_humidity_sensor_type
blue = 0 # Blue colored sensor

# Build file path for JSON output
path = '/home/pi/Desktop/'
fileName = 'MilestoneTwo'
ext = '.json'
# Final file path
filePathName = path + fileName + ext

# Create Dictionary object to store weather data
jsonData = {}
jsonData['weather'] = []



while True:

    try:
        # First parameter is port, second parameter is type of sensor
        [temp,humidity] = grovepi.dht(sensor,blue)
        temp = ((temp * 9) / 5.0) + 32 # Conversion of Celcius to Farenheit
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            # Output temp and humidity data to console
            print("temp = %.02f F humidity = %.02f%%"%(temp, humidity))
            # Set t and h to strings of the numbers
            t = str(temp)
            h = str(humidity)
            # Set background for Display
            setRGB(0,128,64)
            # Output temp and humidity data to display
            setText_norefresh("T:" + t + "F   " + "      H:" + h + "%")

        
        time.sleep(1.0)

            
    except IOError:
        print("Error")
    # Append dictionary with new data
    jsonData['weather'].append({'temperature': t, 'humidity': h})  
    # Write appended dictionary to json file (Overwrite previous file)
    with open(filePathName,'w') as outfile:
        json.dump(jsonData, outfile)
