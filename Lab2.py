valueInArray = int(input("Enter how many numbers you want to write into an array: "))
array = []

for i in range(valueInArray):
  array.append(int(input(f"Enter number {i + 1}: ")))

print(sorted(array))
