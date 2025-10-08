import random
from bubble_sort import bubblesort

# generate a list of 10 random numbers from -100 to 100
number_list = [random.randint(-100,100) for i in range(1000)]
print(f"Initial Values = {number_list}")

outer_pass = 0
inner_pass = 0

sorted_list = bubble_sort(number_list)
print(f"Sorted Values = {sorted_list}")