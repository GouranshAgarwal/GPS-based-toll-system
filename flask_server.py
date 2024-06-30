from flask import Flask, request, jsonify
from database import org,tollZones,nationalHighways as NH

previous_coord=[]

def car_travelling_on_toll_road(coord):
    global previous_coord

    on_road=org.is_vehicle_on_any_toll_road(coord,NH)
    zone=org.return_toll_zone_and_tax_rate(coord,tollZones)
    previous_zone=org.return_toll_zone_and_tax_rate(previous_coord,tollZones)

    if on_road[0]:
        print("car is travelling on toll road")
        if zone[1]!=previous_zone[1]:
            org.zone_wise_distance_toll_collection(previous_zone[2])
            org.entity.coordinates.clear()
        car_coord=f'{coord[0]},{coord[1]}'
        org.entity.coordinates.append(car_coord)
    else:
        envoice=org.zone_wise_distance_toll_collection(zone[2])
        if envoice==False:
            print("car not travelling on toll road")
        else:
            org.entity.coordinates.clear()

    previous_coord=[coord[0],coord[1]]


app = Flask(__name__)

@app.route('/gps', methods=['POST'])
def receive_gps():
    global previous_coord

    if request.is_json:
        data = request.get_json()

        if data and 'latitude' in data and 'longitude' in data:
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if previous_coord==[]:
                previous_coord=[latitude,longitude]

            print(f"Received GPS coordinates: Latitude={latitude}, Longitude={longitude}")
            car_travelling_on_toll_road([latitude,longitude])

            return jsonify({"message": "Coordinates received"}), 200
        else:
            return jsonify({"error": "Invalid coordinates"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/shutdown', methods=['GET'])
def shutdown_server():
    for envoice in org.envoices:
        print(envoice[0])
    print(org.total_toll_collection())

    return jsonify({"message": "Server shutting down"}), 200
 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
