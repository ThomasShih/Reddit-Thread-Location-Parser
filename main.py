from tools.getTextFromReddit import redditScraper
from tools.mapLocater import geoLocater
from tools.plot import plot
import pandas
import sys
import argparse
from tqdm import tqdm

class redditLocation:
    def __init__(self,url,method='geopy'):
        #initialize
        self.url = url
        self.reddit = redditScraper()
        self.geoLocater = geoLocater(method)
    def comments(self):
        self.reddit.getSubmission(url)
        self.reddit.getComments()
    def getLocation(self,testConnections=False):
        resultArray=[]
        dataFrameColumns = ["display_name","type","lon","lat"]
        for comment in tqdm(self.reddit.comments[0] if testConnections else self.reddit.comments,desc="Looking for addresses"):
            #Iterate through possible search entries
            resultArray = resultArray + self.geoLocater.getFromComment(comment)
        
        try: self.locations = pandas.DataFrame(resultArray)[dataFrameColumns].drop_duplicates()
        except: 
            print("Unable to build a dataframe of locations, this is most likely due to an error with connecting to Nominatim")
            self.locations=pandas.DataFrame(columns=dataFrameColumns)
        return self.locations
    def plotLocations(self):
        if self.locations.empty: print("Cannot Plot, Dataframe is empty")
        else: plot(self.locations)
    def export(self,fileName):
        self.locations.to_csv(fileName)

if __name__ == "__main__":
    testConnections = False
    url = sys.argv[1]
    outputLocation = sys.argv[2]
    print("Parsing reddit thread of: {} \n And outputting data to: {}".format(url,outputLocation))

    print("Grabbing Thread From Reddit")
    method = 'geopy'
    redditLocation = redditLocation(url)
    redditLocation.comments()

    redditLocation.getLocation(testConnections=testConnections)

    redditLocation.export(outputLocation)

    redditLocation.plotLocations()