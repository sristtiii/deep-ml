def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	totalarr =[]
	
	if (len(a)!=len(b)):
		return -1
	
	for i in range(len(a)):
		for j in range(len(b)):
			if i==j:
				totalarr.append(a[i]+b[j])
	return totalarr