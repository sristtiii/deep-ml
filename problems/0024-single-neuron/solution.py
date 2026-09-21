import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	
	z_predictions =[]
	for i in range(len(features)):
		total =0
		for j in range(len(features[0])):
			total+=(weights[j]* features[i][j])
		z_predictions.append(total+bias)

	# print(z_predictions)
	
	actual_prediction=[]
	#y = 1/(1+e**-z)

	for i in range(len(z_predictions)):
		value = 1/(1+ (math.exp(-z_predictions[i])))
		actual_prediction.append(value)
	
	# print(actual_prediction)

	# idk if mse has to found or Binary cross entrpyu to be found

	#if mse 1/2n summation(actual -perodtio)**2
	total=0
	for i in range(len(labels)):
		total += ((labels[i]-actual_prediction[i])**2)
	
	total /=(len(labels))

	# print(total)
	final_return_list=[]
	final_return_list.append(actual_prediction)
	final_return_list.append(total)
	my_tuple= tuple(final_return_list)
	return my_tuple
	# if Binary cross entroy 
	# -1/2n(y log predit)+(1-y) log(1-) p)
	# i dont know whih to find 