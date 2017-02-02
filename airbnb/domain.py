

class listing(object):
    def __init__(self,dict):
        #self.__dict__ = json.loads(jsonString)
        z = dict.get('listing')
        self.bathrooms = z.get('bathrooms')
        self.bedrooms = z.get('bedrooms',0)
        self.beds = z.get('beds')
        self.person_capacity =z.get('person_capacity')
        self.name = z.get('name')
        self.lat = z.get('lat')
        self.long = z.get('lng')
        self.property_type = z.get('property_type')
        self.is_new_listing = z.get('is_new_listing')
        self.is_superhost = z.get('is_superhost')
        self.reviews_count=z.get('reviews_count')
        self.room_type_category = z.get('room_type_category')
        self.star_rating = z.get('star_rating')

class price(object):
    def __init__(self,dict):
        z = dict.get('pricing_quote')
        self.price_quote = z
        self.price = z.get('price',0)
        self.rate_with_service_fee=z.get('rate_with_service_fee',None).get('amount')
        self.can_instant_book = z.get('can_instant_book')
