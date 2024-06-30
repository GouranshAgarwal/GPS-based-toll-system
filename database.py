from class_defination import Organizer

# Vehicle Information
vehicle_number = 5674
vehicle_type = "Car"
vehicle_class = "Light Vehicle"

# Back Information
car_gps_id = ''
issuer_bank = ''
back_account=''
account_holder_name=''

# Driver/Owner Information
owner_name = ''
contact_number = ''
email_address = ''




points_geojson = 'geo_data/INDIA_NATIONAL_HIGHWAY.geojson'
# zones_geojson = 'geo_data/Indian_States.geojson' 
zones_geojson = 'geo_data/square_zone.geojson' 

org=Organizer(vehicle_number)
nationalHighways = org.load_national_highways(points_geojson)
tollZones = org.load_toll_zones(zones_geojson)


