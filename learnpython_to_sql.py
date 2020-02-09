import praw
import pandas as pd
import config
import time
#SQL
from sqlalchemy import create_engine

#connects to reddit praw object using my reddit application api client id and client secret
def reddit_object():

    reddit = praw.Reddit(client_id = config.client_id,
                        client_secret = config.client_secret,
                        user_agent = config.user_agent,
                        username = config.username,
                        password = config.password)

    return reddit

#Calls up to the last 1000 submissions from learnpython
def scrape_submissions_1000(reddit):
    sub_list = []
    # selects the subreddit learnpython.  This can be changed to any subreddit
    subreddit = reddit.subreddit('learnpython')
    # have it currently calling100 submissions at a time, but can be any number between 1 and 1000
    for submission in subreddit.new(limit=100):
        # different submission attributes I choose to pull are below
        # look at the praw documentation for other submission attributes
        author = str(submission.author)
        dates = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(submission.created_utc))
        permalink = submission.permalink
        text = submission.selftext
        title = submission.title
        pk = submission.id
        direction = submission.link_flair_text

        sub_list.append([pk, dates, title, text, direction, author, permalink])
    df = pd.DataFrame(sub_list, columns=['id', 'date', 'title', 'text', 'direction', 'author', 'link'])

    return df


def new_submissions(df):
    # SQL connection
    engine = create_engine("mysql+mysqlconnector://{user}:{pw}@{host}/{db}"
                           .format(user=config.user,
                                   pw=config.passwd,
                                   host=config.host,
                                   db=config.db_name))
    # pulls full table from sql
    df_sql = pd.read_sql_table("learnpython",
                               con=engine)

    df_sql.drop('index', axis=1, inplace=True)
    # Checks for only the new rows in the df
    new_submission = df[~df['id'].isin(df_sql['id'])]
    new_sub_list = new_submission.values.tolist()
    return new_sub_list, new_submission, df_sql


def sql_submit(new_submission):
    engine = create_engine("mysql+mysqlconnector://{user}:{pw}@{host}/{db}"
                           .format(user=config.user,
                                   pw=config.passwd,
                                   host=config.host,
                                   db=config.db_name))

    # Insert whole DataFrame into MySQL
    new_submission.to_sql('learnpython', con = engine, if_exists = 'append')


def main():
    reddit = reddit_object()
    df = scrape_submissions_1000(reddit)
    new_sub_list, new_submission, df_sql = new_submissions(df)
    print(new_submission.shape)
    sql_submit(new_submission)


main()







