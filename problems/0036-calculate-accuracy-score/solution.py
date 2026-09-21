import numpy as np

def accuracy_score(y_true, y_pred):
	#TP=11
	#TN=00
	#FP=01
	#FN=10
	tn=0
	tp=0
	fp=0
	fn=0

	for i in range(len(y_true)):
		for j in range(len(y_pred)):
			if i==j:
				if y_true[i]==1 and y_pred[j]==1:
					tp+=1
				elif y_true[i]==0 and y_pred[j]==0:
					tn+=1
				elif y_true[i]==0 and y_pred[j]==1:
					fp+=1
				else:
					fn+=1
	
	return (tn+tp)/(tn+tp+fn+fp)