import json, urllib2

class TransitStop(object):
    partition_key = None
    row_key = None
    time_stamp = None
    stop_id = None
    stop_name = None
    on_street = None
    at_street = None
    lon = None
    lat = None
    facing_direction = None

    def json_dict_to_object(self, json=None):
        object = TransitStop()
        if json is not None:
            object.partition_key = json.get('PartitionKey', None)
            object.row_key = json.get('RowKey', None)
            object.time_stamp = json.get('Timestamp', None)
            object.stop_id = json.get('STOPID', None)
            object.stop_name = json.get('STOPNAME', None)
            object.on_street = json.get('ONSTREET', None)
            object.at_street = json.get('ATSTREET', None)
            object.lon = json.get('LON', None)
            object.lat = json.get('LAT', None)
            object.facing_direction = json.get('FACINGDIR', None)
        return object


def get_all_stops():
    stops = []
    urlopen = urllib2.urlopen('http://openregina.cloudapp.net:8080/v1/OpenRegina/TransitStops/?format=json')
    response = urlopen.read()
    json_data = json.loads(response)
    for stop in json_data.get('d', []):
        stops.append(TransitStop.json_dict_to_object(stop))
    return stops
