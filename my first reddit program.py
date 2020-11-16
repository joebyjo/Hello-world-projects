import praw
import time
reddit = praw.Reddit(client_id="5iavjdrGXIQrQg",
                     client_secret="kl9eNT2BEJAzX1XCQ5MfAVQkmyI",
                     user_agent="MyFirstScript")

subreddit = reddit.subreddit('dpsdubai')

hot_python = subreddit.new()
authors = []
not_need = ["AutoModerator", "nice-scores"]
num = 0

for submission in subreddit.new():
    comments = submission.comments.list()
    for comment in comments:
        if comment.author.total_karma > 1 and comment.author not in authors and comment.author not in not_need:
            authors.append(comment.author)
            num += 1
            print(f"[{num}] https://www.reddit.com/user/{comment.author}/ , {comment.author.total_karma}")
            time.sleep(2)