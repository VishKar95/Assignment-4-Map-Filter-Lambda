numbers = (1, 2, 3, 4, 5, 6, 7) 

print("Original list: ", numbers)

res = map(lambda x: x + x + x, numbers) 

print("\nTriple of list numbers:")
print(list(res))