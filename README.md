This project is a simple disease simulation, all settings are set in tools/attributes.py
An example of the results of this script is 'ExampleResults.csv', this file was generated by inputting reddit url 'https://www.reddit.com/r/solotravel/comments/fzcrci/what_are_your_most_overrated_and_underrated/'

before running the script, run `pip install -r requirements.txt`

afterwards, configure simulation settings and execute script by using `python main.py {redditUrl} {outputFile}`

redditUrl : url of the reddit thread in question, or its id code

outputFile: the file name you want the results to output to (CSV format)



Both arguments are mandatory, or else exception will occur.

To test connection, one can modify testConnections to True to see if the script can connect to Nominatim and such.



Before doing anything, an individual needs to create a credential.py file with reddit API keys as such:

'reddit_client_id={your client ID}

reddit_client_secret={your secret key}

user_agent="LocationGathering"

'

You can set up an reddit API account by going to https://www.reddit.com/prefs/apps

This script uses these very helpful libaries:
tqdm
pandas
plotly
geopy
geograpy3
praw

Arguments

-h, --help          show this help message and exit

-t                  Extracts and looks up one location, for verification that everything is working

-p                  Plots the results on a worldmap, to be displayed through your default browser

-code -c            Reddit URL or post Code (typically 6 character code found in shortlink). Defaults to fzcrci.

-outputLocation -o  Output file path and name of the parsed datafile, default csv if no extension is provided. Supports CSV,xlsx,json. Defaults to .csv

-v                  Verbose
