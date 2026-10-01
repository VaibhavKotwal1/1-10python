#revers the accepted string 
my_string = "India is bharat"
words = my_string.split()
words = words[::-1]

result = " ".join(words)
print(result)