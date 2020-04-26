# Reddit Flair Detector
## Table of Contents
* About the App
* Installation
* Data Collection
* Features Used
* Flair Classification
* Deploying as a web service
* References

### About the App
A Web App based on Python's micro web framework Flask illustrating the task of data aquisition of reddit posts from the r/india subreddit, classification of the posts into 12 different flairs and deploying the best model as a web service by utilising Machine Learning and NLP algorithms. The app can be used here ###

### Installation
Note: The following installation has been tested on Ubuntu 16.04.
This project requires Python 3 and the following Python libraries installed(plus others):

* praw
* scikit-learn
* nltk
* Flask
* Gensim
* pandas
* numpy
* gunicorn
* Matplotlib

#### Steps to run the project locally:
1. Clone the repository
git clone 
cd Reddit-Flair-Detection/
Run
pip install -r requirements




### Data Collection

The task is to perform data aquisition of reddit posts from the /india subreddit, classification of the posts into 12 different flairs and deploying the best model as a web service.
1. Fetched 52,000(1,000 per week) India subreddit data for each of the 12 flairs using PRAW API from reddit.
2. The data includes columns like title, comments, selftext, url, number of comments, score, link_flair_text.
3. Unfortunately the posts have not been tagged with their comments in the dataset. To extract this information, used PRAW for this task.
4.

## Features Used



## 



