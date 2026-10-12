import numpy as np


def calculate_bm25_scores(corpus, query, k1=1.5, b=0.75):
	total_no_of_doc = len(corpus)  # N
	total_no_of_word_in_each_doc = []  # each doc how many words
	for doc in corpus:
		count = 0
		for word in doc:
			count += 1
		total_no_of_word_in_each_doc.append(count)
	mean = 0
	for i in total_no_of_word_in_each_doc:
		mean += i
	mean = mean / total_no_of_doc
	total_no_of_query = len(query)
	frequency_of_each_query = []
	for word in query:
		count = 0
		for doc in corpus:
			if word in doc:
				count += 1
		frequency_of_each_query.append(count)

	idf = []
	for i in range(total_no_of_query):
		df =frequency_of_each_query[i]
		if df == total_no_of_doc:
			idf.append(0)
		else:
			#num = total_no_of_doc - df + 0.5
			#deno = df + 0.5
			#total = (num / deno)+1
			idf.append(np.log((total_no_of_doc + 1) / (df + 1)))
	# here we wil have the ids of the queries
	# now we have to calcuate the score of each query in each document finall add the query(if tere is 2 queries sum them up for one document)

	scores = []  # this will be the 2row 3 col matrix for this partivlar problem
	for i in range(total_no_of_doc):
		each_score = 0
		doc = corpus[i]
		for j in range(total_no_of_query):
			tf = 0
			for word in doc:
				if word == query[j]:
					tf += 1

			term1 = idf[j]
			term2_num = tf * (k1 + 1)
			term2_den = tf + (k1) * (1 - b + b * (len(doc) / mean))
			if term2_den != 0:
				each_score += term1 * (term2_num / term2_den)
		scores.append(each_score)
	return np.round(scores, 3)
