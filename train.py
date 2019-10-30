import nltk
import pickle
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# this part of the code is shamelessly borrowed from:
# https://www.twilio.com/blog/2017/09/sentiment-analysis-python-messy-data-nltk.html
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

pos = []
with open("rt.pos", encoding="utf8") as f:
    for i in f:
        pos.append([format_sentence(i), 'pos'])

neg = []
with open("rt.neg", encoding="utf8") as f:
    for i in f:
        neg.append([format_sentence(i), 'neg'])

# next, split labeled data into the training and test data
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]

# a second test data set based on tweets
test_2 = []
with open("pos_tweets.txt", encoding="utf8") as f:
    for i in f:
        test_2.append([format_sentence(i), 'pos'])

with open("neg_tweets.txt", encoding="utf8") as f:
    for i in f:
        test_2.append([format_sentence(i), 'neg'])

classifier = NaiveBayesClassifier.train(training)
classifier.show_most_informative_features()
print("accuracy = " + str(accuracy(classifier, test)))
print("accuracy 2 = " + str(accuracy(classifier, test_2)))

# training a model every time we run the program is inefiicient
# we use pickle to store and save the model for future use
classifier_file = open("classifier.pickle", "wb")
pickle.dump(classifier, classifier_file)
classifier_file.close()