# Vehicle Toll Tracking System and GPS Toll Collection System

## Overview
This project is a vehicle toll tracking system that uses GPS coordinates to determine if a vehicle is on a toll road. The system integrates with a REST API, processes GPS data, and calculates toll fees based on the vehicle's distance traveled on toll roads.

## Features
- *Entity Tracking*: Manage vehicle information and track their travel distance.
- *GeoJSON Integration*: Load national highways and toll zones from GeoJSON files.
- *API Integration*: Use the OSRM API to calculate the distance between GPS coordinates.
- *Flask Server*: Receive GPS coordinates via a POST request and process them to check if the vehicle is on a toll road.
- *Toll Calculation*: Calculate toll fees based on the distance traveled.

## Prerequisites
- Python 3.x
- Flask
- GeoPandas
- Requests
- Shapely

## Installation
1. Clone the repository:
    bash
    git clone https://github.com/yourusername/vehicle-toll-tracking.git
    
2. Navigate to the project directory:
    bash
    cd vehicle-toll-tracking
    
3. Create and activate a virtual environment:
    bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    
4. Install the required packages:
    bash
    pip install Flask GeoPandas Requests Shapely
    

## Usage

### Run the Flask server:
    python flask_server.py

### Sending GPS Data
Run the script to send GPS data: client.py

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgements
- [OSRM Project](http://project-osrm.org/)
- [GeoPandas](https://geopandas.org/)
- [Shapely](https://shapely.readthedocs.io/)
