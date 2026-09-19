import numpy as np

def dice_score(y_true, y_pred):
	
	tp=0
	tn=0
	fp=0
	fn=0
	for i in range(len(y_pred)):
		if(y_true[i]==1 and y_pred[i]==1):
			tp+=1
		elif(y_true[i]==0 and y_pred[i]==0):
			tn+=1
		elif(y_true[i]==0 and y_pred[i]==1):
			fp+=1
		else:
			fn+=1
	if (tp + fp) == 0 or (tp + fn) == 0:
        return 0.0
			
	precision = tp/(tp+fp)
	recall = tp/(tp+fn)
	if (precision + recall) == 0:
        return 0.0
	f1=(2*(precision*recall))/ (precision+recall)
	return np.round(f1,3)