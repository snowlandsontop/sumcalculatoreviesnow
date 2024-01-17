#ask user for positive number
num = int(input("Enter a positive number: "))

# initialize the couner
count = 1

#initialize the sum
sum = 0

while (count <= num):
  sum = sum + count
  count = count + 1

print ("the sum of the numbers from 0 to and including", num, "is", sum)