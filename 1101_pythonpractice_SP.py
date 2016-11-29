# def square (x):
# 	return (x * x)

# a = square(13)
# print a


# def favorite_color(name): 
# 	names = {'Stephanie' : 'blue',  'Ava' : 'blue', 'Crystal' : 'blue', 'Elena' : 'silver', 'Odelia' : 'none', 'Renee' : 'purple'}
# 	print names[name]
# 	return

# favorite_color(raw_input(''))

def reverse (lst):
	lst = [1,2,3,4]
	new_lst = []
	index = len(lst) -1
	while index >= 0:
		new_lst.append(lst[index])
		index = index -1
	return new_lst
