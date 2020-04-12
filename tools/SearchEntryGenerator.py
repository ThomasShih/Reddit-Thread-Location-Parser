import geograpy3

def SearchEntryGenerator(inputString,want='all'):
    try: 
        places = geograpy3.get_place_context(text = inputString)
        if want=="cities":locations = places.cities
        elif want=="regions":locations = places.regions
        elif want=="countries":locations = places.countries
        elif want=="all":locations = places.cities + places.regions + places.countries + places.other
        locations = list(set(locations)) #Remove Duplicates
    except:
        locations = []
    return locations

if __name__ == "__main__":
    inputString = "Luang Prabang right on the river not too busy and a great night, New York, Califorina and Canada are also really nice choices"

    for i in SearchEntryGenerator(inputString,'all'):
        print(i)