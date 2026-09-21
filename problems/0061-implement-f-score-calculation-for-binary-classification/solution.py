import numpy as np
def f_score(y_true, y_pred, beta):
	# f score = 2* precision *recal/(precsiio+recall)
	# in f1 if there is beta then 
	# (1+B**2)*precision*recall
	#---------------------------
	# (B**2)*precision)+recall
	tp=0
	tn=0
	fp=0
	fn=0

	for i in range(len(y_true)):
		for j in range(len(y_pred)):
			if(i==j):
				if(y_true[i]==1 and y_pred[j]==1):
					tp+=1
				elif(y_true[i]==0 and y_pred[j]==0):
					tn+=1
				elif(y_true[i]==0 and y_pred[j]==1):
					fp+=1
				elif(y_true[i]==1 and y_pred[j]==0):
					fn+=1
				else:
					pass
	precision = tp/(tp+fp)
	recall =tp/(tp+fn)

	betaa =(1+(beta**2))

	numerator = betaa*precision*recall
	denominator = ((beta**2)*precision )+recall

	return np.round(numerator/denominator,4);