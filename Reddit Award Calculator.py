import csv
import praw
from config import *

# todo comment id finder
# todo .csv file maker
# todo subbreddit id to identify the subreddit
r = praw.Reddit(client_id= REDDIT_CLIENT_ID,
                client_secret=REDDIT_CLIENT_SECRET,
                user_agent="MyFirstScript")

exceptions = {"Platinum": 700,
              "Mindblowingly Cool Post": 700,
              "Great Contributions to /r/pics": 700}

def award_calc(id, SorC="s"):
    submission = None
    if SorC == "s":
        submission = r.submission(id)

    elif SorC == "c":
        submission = r.comment(id)
    total_coins = 0
    total_premium = 0
    total_count = 0
    total_coin_reward = 0
    for award in submission.all_awardings:
        if award["name"] in exceptions:
            if award["name"] == "Platinum":
                award['coin_reward'] = exceptions["Platinum"]
            if award["name"] == "Mindblowingly Cool Post":
                award['coin_reward'] = exceptions["Mindblowingly Cool Post"]
            if award["name"] == "Great Contributions to /r/pics":
                award['coin_reward'] = exceptions["Great Contributions to /r/pics"]

        total_coins += int(award['coin_price']) * int(award["count"])
        total_count += int(award['count'])
        total_coin_reward += int(award['coin_reward']) * int(award["count"])

        if int(award['days_of_premium']):
            total_premium += int(award['days_of_premium']) * int(award["count"])

        print(award['name'], int(award['count']), int(award['days_of_premium'] * award['count']),
              int(award['coin_reward']), sep="--")

    print(f'''
    
Total coins spent:{total_coins}
Total premium:{total_premium}
Total count:{total_count}
Total coin reward:{total_coin_reward}
Dollars spent:{total_coins / 500 * 1.99}$
    ''')


def awards_list(id,SorC="s"):
    submission = None
    if SorC == "s":
        submission = r.submission(id)

    elif SorC == "c":
        submission = r.comment(id)
    f = open(f'Reddit_Awards.csv', 'a', newline='')
    writer = csv.writer(f)
    if 'Name of award' not in open('Reddit_Awards.csv').read():
        writer.writerow(['Name of award', 'Coin Price', 'Days of Premium', 'Coin Reward'])
    for award in submission.all_awardings:
        if award["name"] in open('Reddit_Awards.csv').read():
            pass
        else:
            writer = csv.writer(f)
            writer.writerow([award['name'], award['coin_price'], award['days_of_premium'], award['coin_reward']])
            print(award['name'], award['coin_price'], award['days_of_premium'], award['coin_reward'])
    f.close()


awards_list('eewq6i', 's')
