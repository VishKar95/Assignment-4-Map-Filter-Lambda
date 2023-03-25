def square_num(s):
  return s * s

numbers = [4, 5, 2, 9]

print("Original List: ",numbers)

res = map(square_num, numbers)

print("Square the elements of the list :")
print(list(res))