import pickle
import nltk


def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

classifier_file = open("classifier.pickle", "rb")
classifier = pickle.load(classifier_file)
classifier_file.close()

tweets_file = open("tweet_data.txt", "r", encoding="utf-8")
tweets_list = tweets_file.readlines()

score = 0
for tweet in tweets_list:
    tweet.rstrip()
    tweet = tweet.replace("\r", "")
    tweet = tweet.replace("\n", "")
    #print(tweet + " : " + classifier.classify(format_sentence(tweet)))
    if classifier.classify(format_sentence(tweet)) == "pos":
        score = score + 1
print("num tweets is: " + str(len(tweets_list)))
print("num pos tweets is: " + str(score))
print("num neg tweets is: " + str(len(tweets_list)-score))
print("score is : " + str((score/len(tweets_list))*100) + "% positive")
