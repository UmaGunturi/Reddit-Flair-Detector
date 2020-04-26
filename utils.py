import json
from urllib.request import urlopen
import praw
import re
import os
from nltk import word_tokenize
import pickle
import joblib
reddit = praw.Reddit(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'], user_agent=os.environ['user_agent'], username=os.environ['username'], password=os.environ['password'])
STOPWORDS = set(open('english_stopwords').read().split('\n'))


def cleaning(text):
    text = str(text).lower()
    tokens = word_tokenize(text)
    text = ' '.join(
        word for word in tokens if word not in STOPWORDS and word.isalpha())
    return text


def clean_url(url):
    non_uselful = ['http', 'https', 'www', 'com', 'reddit']
    add_ons = ['cms', 'comments', 'r', 'redd', 'google', 'amp', 'co',
               'youtu', 'india', 'jpg', 'article', 'youtube', 'png', 'twitter']
    non_uselful += add_ons
    non_uselful = set(non_uselful)
    delimiters = [':', '/', '_', '-', '.']
    pattern = '|'.join(map(re.escape, delimiters))
    try:
        url = re.split(pattern, url)
    except:
        return ''
    else:
        url = ' '.join(word for word in url if word not in STOPWORDS and
                       word.isalpha() and word not in non_uselful)
        return url


def get_flair(url):
    submission = reddit.submission(url=url)
    title, f_url, selftext = cleaning(submission.title), clean_url(
        submission.url), cleaning(submission.selftext)
    comments = ''
    submission.comments.replace_more(limit=None)
    for comment in submission.comments:
        comments += ' ' + comment.body
    comments = cleaning(comments)
    all_content = " ".join([title, f_url, selftext, comments])
    # model = pickle.load(open('final_model.pkl', 'rb'))
    model = joblib.load('model.pkl')
    res = model.predict([all_content])
    return res[0]


if __name__ == "__main__":
    get_content(
        'https://www.reddit.com/r/india/comments/g40et7/indias_cases_jumped_from_14352_on_apr_17_to_16365/')
