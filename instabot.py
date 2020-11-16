# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'joebyjo_2'  # <- enter username here
insta_password = 'iamjoe123'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username="joebyjo_2",
                  password="iamjoe123")

with smart_run(session):
    """ Activity flow """
    # general settings


    # sets the percentage of people you want to follow
    session.set_do_follow(True, percentage=50)

    # setting quotas for the daily and hourly action
    session.set_quota_supervisor(enabled=True, peak_comments_daily=250, peak_comments_hourly=30, peak_likes_daily=250,
                                 peak_likes_hourly=30, sleep_after=['likes', 'follows'])

    # again some set of configuration which figures out whom to follow
    relationship_bounds = session.set_relationship_bounds(enabled=True,
                                                          delimit_by_numbers=True,
                                                          max_followers=3000,
                                                          min_followers=150,
                                                          min_following=150)

    if relationship_bounds:
        session.set_do_follow(True, percentage=50)

    # tags to get posts from and amout is the actions you want
    session.like_by_tags(['valorant', 'memes', 'food', 'pubity'], amount=300)

session.end()
