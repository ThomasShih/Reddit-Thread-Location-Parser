This project is a simple disease simulation, all settings are set in tools/attributes.py
An example of the results of this script is 'ExampleResults.csv'

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