from getTextFromReddit import redditScraper
from mapLocater import geoLocater
from plot import plot
import pandas
from tqdm import tqdm
method = 'geopy'

if __name__ == "__main__":
    print("Grabbing Thread From Reddit")
    reddit = redditScraper()
    reddit.getSubmission("https://old.reddit.com/r/solotravel/comments/fyfz0l/the_most_atmospheric_city_youve_visited/")
    reddit.getComments()
    #reddit.cleanComments()

    print("Intialitizing Geolocater")
    geoLocater = geoLocater(method)

    resultArray=[]
    for comment in tqdm(reddit.comments,desc="Looking for addresses"):
        #Iterate through possible search entries
        resultArray = resultArray + geoLocater.getFromComment(comment)

    locations = pandas.DataFrame(resultArray)[["display_name","type","lon","lat"]].drop_duplicates()
    locations.to_csv("results.csv")
    plot(locations)