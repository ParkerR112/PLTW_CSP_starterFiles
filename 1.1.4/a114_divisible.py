#   a114_divisible.py

# get two numbers from user
a = float(input('Number 1'))
b = float(input('Number 2'))
# loop whle the numbers are not divisible (the remainder is 0)
while a % b != 0:
  # inform user of result 
  print("these numbers are not divisable")
  # gather user input again
  a = float(input('Number 1'))
  b = float(input('Number 2'))
# inform user of result 
print(a/b)