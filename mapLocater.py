from geopy.geocoders import Nominatim as geocoder
from SearchEntryGenerator import SearchEntryGenerator
from pprint import pprint as pp
class geoLocater:
    def __init__(self,method='geopy',tries=3):
        if method=='geopy':
            self.geolocator = geocoder(user_agent="redditMapGenerator")
            self.tries = tries
    def get(self,searchQuery):
        for i in range(self.tries):
            try: return self.geolocator.geocode(searchQuery,language="en")
            except: pass
        return None
    def getFromComment(self,comment):
        results=[]
        for searchEntry in SearchEntryGenerator(2,comment):
            result = self.get(searchEntry)
            if result and result not in results:
                results.append(result.raw)

        return results


if __name__ == "__main__":
    a = geoLocater()

    print(a.get("Shouldn't return a result"))