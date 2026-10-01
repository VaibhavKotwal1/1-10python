#accept 2 values s and n . print square of first N numbers starting from s
s = int(input("Enter starting number (s): "))
n = int(input("Enter how many numbers (n): "))

i = 0
while i < n:
  current_num = s + i
  print(f"Square of {current_num} = {current_num ** 2}")
  i += 1