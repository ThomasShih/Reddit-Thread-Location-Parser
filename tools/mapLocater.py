from geopy.geocoders import Nominatim as geocoder
from tools.SearchEntryGenerator import SearchEntryGenerator

class geoLocater:
    def __init__(self,verbose=False):
        self.geolocator = geocoder(user_agent="redditMapGenerator")
        self.verbose = verbose
    def get(self,searchQuery):
        for i in range(3): #try three times to connect to Nominatim, its sometimes unreliable
            try:
                return self.geolocator.geocode(searchQuery,language="en",timeout=3) #wait three seconds before timeout, this is because Nominatim is slow sometimes
            except: print("Could not get location for {}, this is most likely a timeout issue.".format(searchQuery))
        return None
    def getFromComment(self,comment):
        results=[]
        for searchEntry in SearchEntryGenerator(comment,want='all'):
            if self.verbose: print("\nLooking for {} from =>: {}".format(searchEntry,comment.replace("\n"," ")))
            result = self.get(searchEntry)
            if result:
                results.append(result.raw)
        return results


if __name__ == "__main__":
    a = geoLocater()

    print(a.get("Shouldn't return a result"))