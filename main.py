#Check to make sure credential.py exists first
try: from credential import reddit_client_id,reddit_client_secret,user_agent
except: 
    print("Please create a credential.py file, exiting gracefully")
    import sys
    sys.exit()

import argparse
parser = argparse.ArgumentParser(description="Gathers mentions of locations and cities from a Reddit post")
parser.add_argument('-t',help="Extracts and looks up one location, for verification that everything is working",action='store_true')
parser.add_argument('-p',help="Plots the results on a worldmap, to be displayed through your default browser",action='store_true')
parser.add_argument('-code',metavar="-c",type=str,help="Reddit URL or post Code (typically 6 character code found in shortlink). Defaults to fzcrci.",default=None)
parser.add_argument('-outputLocation',metavar="-o",type=str,help="Output file path and name of the parsed datafile, default csv if no extension is provided. Supports CSV,xlsx,json. Defaults to results.csv",default=None)
parser.add_argument('-v',help="Verbose",action='store_true')
args = parser.parse_args()

if args.t:
    if args.code == None: args.code = "fzcrci"
    if args.outputLocation == None: args.outputLocation = "test.csv"
elif args.code == None or args.outputLocation == None:
    print("Not in testing mode, please provide values for code and outputLocation, -h for help")
    import sys
    sys.exit()

import pandas
from tqdm import tqdm

from tools.getTextFromReddit import redditScraper
from tools.mapLocater import geoLocater

class redditLocation:
    def __init__(self):
        #initialize
        self.reddit = redditScraper()
        self.geoLocater = geoLocater(verbose=args.v)
    def comments(self):
        self.reddit.getSubmission(args.code)
        self.reddit.getComments()
    def getLocation(self,testConnections=False):
        resultArray=[]
        dataFrameColumns = ["display_name","type","lon","lat"]
        comments = [self.reddit.comments[0]] if args.t else self.reddit.comments
        for comment in tqdm(comments,desc="Looking for addresses"):
            #Iterate through possible search entries
            resultArray = resultArray + self.geoLocater.getFromComment(comment)
        
        try: self.locations = pandas.DataFrame(resultArray)[dataFrameColumns].drop_duplicates()
        except: 
            print("Unable to build a dataframe of locations, this is most likely due to an error with connecting to Nominatim")
            self.locations=pandas.DataFrame(columns=dataFrameColumns)
        return self.locations
    def export(self,fileName):
        print("Exporting Results")
        if fileName.endswith(".xlsx"): self.locations.to_excel(fileName)
        elif fileName.endswith(".json"): self.locations.to_json(fileName)
        elif fileName.endswith(".csv"): self.locations.to_csv(fileName)
        else: self.locations.to_csv(self.filename + ".csv")
    def plotLocations(self):
        from tools.plot import plot
        if self.locations.empty: print("Cannot Plot, Dataframe is empty")
        else: plot(self.locations)

if __name__ == "__main__":
    print("Parsing reddit thread of: {} \nAnd outputting data to: {}".format(args.code,args.outputLocation))

    print("Grabbing Thread From Reddit")
    redditLocation = redditLocation()
    redditLocation.comments()

    redditLocation.getLocation()

    redditLocation.export(args.outputLocation)

    if args.p:
        redditLocation.plotLocations()