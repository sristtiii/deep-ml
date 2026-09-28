
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	
	tp,tn,fp,fn=0,0,0,0

	for i in range(len(actual)):
		if(actual[i]==1 and predicted[i]==1):
			tp+=1
		elif(actual[i]==0 and predicted[i]==0):
			tn+=1
		elif (actual[i]==0 and predicted[i]==1):
			fp+=1
		else :
			fn+=1
	confusion_matrix =[[tp,fn],[fp,tn]]
	accuracy =(tn+tp )/ (tp+tn+fn+fp)
	specificity= tn/(tn+fp)
	negativePredictive = tn/(tn+fn)
	precision = tp/(tp+fp)
	recall = tp/(tp+fn)
	f1 = 2* precision * recall /(precision+recall)
	# f1 = 2*precision * recall/ precisin+recall
	# accuracy ,precision,recall,f1
	# accuracy,specificty ,negative predictive ,f1
	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
