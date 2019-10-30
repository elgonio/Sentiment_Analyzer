with open("pos_tweets.txt") as input_file:
	text = input_file.read()
	text_set = set(text.split(" "))
	for word in text_set:
		print(word,text.count(word))