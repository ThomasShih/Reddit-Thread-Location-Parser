import geograpy4

class geoLocater:
    def __init__(self,verbose=False):
        self.verbose = verbose
    def get(self,searchQuery):
        try: 
            locations = geograpy4.get_place_context(searchQuery,addressOnly=False,ignoreEstablishments=False)
        except Exception as e:
            if self.verbose: print("Error occured locating: {}".format(e))
            locations = []
        return locations
    def getFromComment(self,comment):
        return self.get(comment)


if __name__ == "__main__":
    a = geoLocater()

    print(a.get("Shouldn't return a result"))