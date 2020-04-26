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
A Web App based on Python's micro web framework Flask illustrating the task of data aquisition of reddit posts from the r/india subreddit, classification of the posts into 12 different flairs and deploying the best model as a web service by utilising Machine Learning and NLP algorithms. The app can be used here https://redditflaird.herokuapp.com/

### Installation
Note: The following installation has been tested on Ubuntu 16.04.
This project requires Python 3 and the following Python libraries installed(plus others):

* praw
* scikit-learn
* nltk
* Flask
* pandas
* numpy
* gunicorn
* Matplotlib
* keras

### Data Collection

The task is to perform data aquisition of reddit posts from the /india subreddit, classification of the posts into 12 different flairs and deploying the best model as a web service.
1. Fetched 52,000 (1,000 per week) for the last year, India subreddit data for each of the 12 flairs using Pushshift API.
2. The data includes title, comments, selftext, url, number of comments, score, link_flair_text.
3. Many post do not have a flair associated with them, they will be removed from the dataset.
4. Unfortunately the posts have not been tagged with their comments in the dataset. To extract this information, PRAW is used.

## Features Used

5 types of features are considered for the the given task:


a) ```title```

b) ```comments```

c) ```url```

d) ```selftext```




## Flair-Classification

The following ML algorithms are used to classify:


a) ```Naive-Bayes```

b) ```Linear Support Vector Machine```

c) ```Logistic Regression```

d) ```Random Forest```

e) ```MLP```

f) ```BOW with Keras```

### Accuracies of all the models on different combination of features 

| Feature\Model | Naive-Bayes  | Linear SVM  | Logistic Regression  | Random Forest | MLP | BOW |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| title | 59  | 61  | 60  |  62 | 49  | 62 |
| title + url | 59  | 64  | 64  | 64  | 49  | 59 |
| title + url +selftext  | 60  | 73  | 74  | 75  | 56  | 71 |
| title + url +selftext + comments  | 57  | 74  | 74  | 79  | 58  | 61 |

## Deploying as Web Service

The best model - Random Forest is deployed as a web app. Check the live demo [here](https://redditflaird.herokuapp.com/). The app was deployed using a free service like Heroku. All the required files can be found in the branch ```webapp```.

## References

* https://www.storybench.org/how-to-scrape-reddit-with-python/
* https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
* https://towardsdatascience.com/designing-a-machine-learning-model-and-deploying-it-using-flask-on-heroku-9558ce6bde7b










