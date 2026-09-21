import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	final_dict={}

	total=0
	for i in range(len(gradient)):
		total+=(gradient[i]**2)
	
	final_dict["magnitude"]= np.sqrt(total)
	if (np.sqrt(total) ==0):
		 return {
            "magnitude": 0.0,
            "direction": [0.0] * len(gradient),
            "descent_direction": [0.0] * len(gradient)
        }
	direction=[]
	negative =[]

	for i in gradient:
		direction.append(i/final_dict["magnitude"])
		negative.append(-1*(i/final_dict["magnitude"]))

	final_dict["direction"]= direction
	final_dict["descent_direction"]= negative

	return final_dict

