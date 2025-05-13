#the_largest_of_three_values.py

def maximum(value1, value2, value3):
	"""Return the maximum of three values."""
	max_value = value2
	if value2 > max_value:
		max_value = value2
	if value3 > max_value:
		max_value = value3
	return max_value
	
values = input('Enter the Values: ').split()
value1, value2, value3 = values
	
print(f"The maximum value is: {maximum(value1, value2, value3)}")
