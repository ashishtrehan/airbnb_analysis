import scraper
import Logger
import os.path
import json
import numpy as np
from domain import price

log = Logger.getLogger(__name__)


def pull_data():
     if os.path.exists('json/metadata.json')==True:
         metadata=json.load(open('json/metadata.json','r'))
         listing = json.load(open('json/listing.json','r'))
         return metadata,listing
     else:
         with open('atlneighborhoods.txt') as f:
             neighborhoods = f.readlines()
         neighborhoods = [x.strip('"\n,') for x in neighborhoods]
         metadata,listing=scraper.json_airbnb(neighborhoods)
         return metadata,listing

def neighbor_function(neighborhood):
    metadata,listing=pull_data()
    log.info('Keys for {0}'.format(listing.keys()))
    for x in listing.keys():
        log.info({'Neighborhood':x,'Prices':np.mean([price(z).rate_with_service_fee for z in listing.get(x)])})

def main():
    neighbor_function("'Adamsville/Oakcliff'")
    #log.info('Metadata: {0}'.format(len(0)))
if __name__ == "__main__":
    main()
