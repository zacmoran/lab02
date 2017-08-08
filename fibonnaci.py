def calcFib(num):
	if(num and num != 1): num = calcFib(num-1) + calcFib(num-2);
	return num;
print(calcFib(int(input())));