import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	
	hidden =np.array(initial_hidden_state)
	Wx =np.array(Wx)
	Wh =np.array(Wh)
	b = np.array(b)

	for i in input_sequence:
		x_array=np.array(i)

		input_term = np.dot(Wx,x_array)
		hidden_term =np.dot(Wh,hidden)

		hidden = np.tanh(input_term+hidden_term+b)

	return np.round(hidden,4).tolist()