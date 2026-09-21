import math
def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	# this is asking fr the categorical cross entropy 

	total =0
	for i in logits:
		total+=(math.exp(i))

	softmax = []
	for i in range(len(logits)):
		softmax.append(math.exp(logits[i])/total)
	# print(softmax)

	trag=[]
	for i in range(len(logits)):
		if i==target:
			trag.append(1)
		else:
			trag.append(0)
	# print(trag)

	# in dl what hppens is that the CCE(categorial cross entrypy ) -summationof y* log predion
	# intead taske serivative simplified to p-y

	final_list=[]
	for i in range(len(logits)):
		final_list.append(softmax[i]-trag[i])
	return final_list