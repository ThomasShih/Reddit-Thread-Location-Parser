import praw
from credential import reddit_client_id,reddit_client_secret,user_agent
from tools.stringCleaner import stringCleaner

class redditScraper(stringCleaner):
    def __init__(self):
        self.reddit = praw.Reddit(client_id=reddit_client_id\
                                 ,client_secret=reddit_client_secret\
                                 ,user_agent=user_agent)
    def getSubmission(self,url):
        try: self.submission = self.reddit.submission(url=url)
        except: self.submission = self.reddit.submission(id=url)
    def getComments(self):
        self.comments = []
        for parentComment in self.submission.comments:
            self.comments.append(parentComment.body)

if __name__ == "__main__":
    reddit = redditScraper()
    reddit.getSubmission("https://old.reddit.com/r/solotravel/comments/fyfz0l/the_most_atmospheric_city_youve_visited/")
    reddit.getComments()
    print(reddit.comments)