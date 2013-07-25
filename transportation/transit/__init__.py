import stops
import routes

def _save_google_transit_data(save_path=None):
    if save_path is None:
        print('Will not run without a save_path provided!')
        return


def _get_google_transit_data():

    print('Getting transit information in Google Transit format')
    transit_stops = stops.get_all_stops()
    print('%s stops returned' % (len(transit_stops)))
    transit_routes = routes.get_all_routes()
    print('%s routes returned' % (len(transit_routes)))
    print('Done fetching and compiling transit information')
    return {
        'stops': transit_stops,
        'routes': transit_routes,
        'agency': _create_google_agency_string(),
    }

def _create_google_agency_string():
    agency_string = 'agency_id,agency_name,agency_url,agency_timezone,agency_lang,agency_phone\n'
    agency_string += ',Regina Transit Department,http://www.regina.ca/residents/transit-services/,America/Regina,en,'
    return agency_string

def regina_to_google_transit(save_path=None):
    information = _get_google_transit_data()
    _save_google_transit_data(save_path, information)