def calculate_f1_score(y_true, y_pred):
	# tp -11 ,tn-11, fp-01,fn-10
	# accuracy = tp/n ,precision = tp/tp+fp ,recall =tp/tp+fn
	#f1 score = 2*precosion recall/precision +rcall

	tp=0
	tn=0
	fp=0
	fn=0
	for i in range(len(y_true)):
		if y_true[i]==1 and y_pred[i]==1:
			tp+=1
		elif y_true[i]==0 and y_pred[i]==0:
			tn+=1
		elif y_true[i]==0 and y_pred[i]==1:
			fp+=1
		else:
			fn+=1
	
	precision = tp/(tp+fp) if (tp+fp)>0 else 0.0
	recall = tp/ (tp+fn) if (tp+fn)>0 else 0.0

	if precision+recall ==0:
		return 0.0

	return round((2*(precision*recall))/(precision+recall),3)