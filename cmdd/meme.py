import praw
import config
import random
import config

black_list = config.memes_blacklist_genres
                
reddit = praw.Reddit(   client_id = config.praw_client_id, #reddit client_id
                        client_secret = config.praw_client_secret, #reddit secret id 
                        username = config.praw_username, #reddit username
                        password = config.praw_password, #reddit pass
                        user_agent = config.pwaw_user_agent #user agent (anything is ok)
                    )
def get_meme():
    subreddit = reddit.subreddit("memes")
    all_subs = []

    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    url = random_sub.url
    name = random_sub.title
    return url,name
    

