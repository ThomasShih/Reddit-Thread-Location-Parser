from geopy.geocoders import Nominatim as geocoder
from tools.SearchEntryGenerator import SearchEntryGenerator

class geoLocater:
    def __init__(self,method='geopy',tries=3):
        if method=='geopy':
            self.geolocator = geocoder(user_agent="redditMapGenerator")
            self.tries = tries
    def get(self,searchQuery):
        for i in range(self.tries):
            try: return self.geolocator.geocode(searchQuery,language="en",timeout=3)
            except: print("Could not get location for {}, this is most likely a timeout issue.".format(searchQuery))
        return None
    def getFromComment(self,comment):
        results=[]
        for searchEntry in SearchEntryGenerator(comment,want='all'):
            result = self.get(searchEntry)
            if result:
                results.append(result.raw)
        return results


if __name__ == "__main__":
    a = geoLocater()

    print(a.get("Shouldn't return a result"))