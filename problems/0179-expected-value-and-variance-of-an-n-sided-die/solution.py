def dice_statistics(n: int) -> tuple[float, float]:
	expected =0
	for i in range(1,n+1):
		expected+=i
	total_variance =0;
	for i in range(1,n+1):
		total_variance+=((i-(expected/n ))**2)
	total_variance/=n
	return (expected/n ,total_variance)