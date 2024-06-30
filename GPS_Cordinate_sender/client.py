from re import error
import requests
import time
import subprocess

server_process = subprocess.Popen(['Scripts/python.exe', 'flask_server.py'])

time.sleep(20)

with open('geo_data/Car_Path.txt', 'r') as file:
    lines = file.readlines()

coords = []

for index,line in enumerate(lines):
    if index<180:
        continue
    line = line.strip()
    lon, lat = map(float, line.split(','))
    coords.append([lon,lat])

coords.append([1, 1])

print("sending coordinates: --")

server_url = 'http://localhost:5000/gps'
frontend_url='http://localhost:4000/gps'

for index,coord in enumerate(coords):
    data = {
        'latitude': coord[1],
        'longitude': coord[0]
    }
    response_server = requests.post(server_url, json=data)
    response_frontend = requests.post(frontend_url, json=data)
    print(response_server.json(),index+1)
    time.sleep(1)

time.sleep(5)

print("Server process finished....")

url = 'http://localhost:5000/shutdown'
response = requests.get(url)
print(response.json())
  
time.sleep(1)
print("server closed")