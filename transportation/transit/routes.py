import json
import urllib2


class TransitRoute(object):
    partition_key = None
    row_key = None
    time_stamp = None
    route_number = None
    route_name = None
    to_name = None
    from_name = None
    shape_length = None

    def json_dict_to_object(self, json=None):
        object = TransitRoute()
        if json is not None:
            object.partition_key = json.get('PartitionKey', None)
            object.row_key = json.get('RowKey', None)
            object.time_stamp = json.get('Timestamp', None)
            object.route_number = json.get('ROUTENUM', None)
            object.route_name = json.get('ROUTENAME', None)
            object.to_name = json.get('TO_NAME', None)
            object.from_name = json.get('FROM_NAME', None)
            object.shape_length = json.get('Shape_Leng', None)
        return object


def get_all_routes():
    stops = []
    urlopen = urllib2.urlopen('http://openregina.cloudapp.net:8080/v1/OpenRegina/TransitStops/?format=json')
    response = urlopen.read()
    json_data = json.loads(response)
    for stop in json_data.get('d', []):
        stops.append(TransitRoute.json_dict_to_object(stop))
    return stops