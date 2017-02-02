import requests
import json
import os.path
import Logger


log = Logger.getLogger(__name__)

with open('atlneighborhoods.txt') as f:
    neighborhoods = f.readlines()
neighborhoods = [x.strip('"\n,') for x in neighborhoods]


def airbnb(neighborhood:str):
    url = 'https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&locale=en-US&currency=USD&_format=for_search_results_with_minimal_pricing&_limit=50&_offset=0&fetch_facets=true&guests=1&ib=false&ib_add_photo_flow=true&location=Atlanta%20GA%2C%20US&neighborhoods%5B%5D='
    response = requests.get(url+str(neighborhood))
    return response.json()


def json_airbnb(neighborhoods:list):
    metadata = {}
    listing = {}
    for x in neighborhoods:
        data = airbnb(x.replace("'",""))
        metadata[x]=data.get('metadata')
        listing[x]=data.get('search_results')
    with open('json/metadata.json','w') as outfile:
        json.dump(metadata,outfile)
    with open('json/listing.json','w') as listfile:
        json.dump(listing,listfile)
    return metadata,listing

def main():
    if os.path.exists('json/metadata.json') and os.path.exists('json/listing.json'):
        log.info(os.path.exists('json/metadata.json'))
        return log.info('file path exists:')
    else:
        json_airbnb(neighborhoods)



if __name__ == "__main__":
    main()
