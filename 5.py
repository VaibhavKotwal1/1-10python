#remove duplicate from list
my_list = [5, 1, "Code", 56.32, 5, 5, "om", 1, 1, "om"]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

print(result)