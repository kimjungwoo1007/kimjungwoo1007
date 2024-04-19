numbers = [[1,2,3], [4,5,6], [7,8,9]]
results=[]
for row in numbers :
    for element in row:
        if numbers % 2 ==0:
            results.append(numbers)
print("짝수:",results)
