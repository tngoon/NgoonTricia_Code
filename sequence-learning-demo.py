from numpy import array

#generate a sequence of real values between 0 and 1
def generate_sequence(length=10):
	return array([i/float(length) for i in range(length)])

# print(generate_sequence())
