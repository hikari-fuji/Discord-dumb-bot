import praw
import config
import random

black_list = config.memes_blacklist_genres
                
reddit = praw.Reddit(   client_id = "fc8lB0GHfW5TZwjx_7Vfbg", #reddit client_id
                        client_secret = "aVtar8Cx3mD3ZHNpzTmCNS8KH75l5w", #reddit secret id 
                        username = "Hikari_fuji", #reddit username
                        password = "hongungok", #reddit pass
                        user_agent = "Hikari Fuji" #user agent (anything is ok)
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
    

