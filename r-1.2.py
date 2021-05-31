def minmax(data):
    smallest=largest=data[0] 
    for entry in data:
        if smallest > entry:
            smallest = entry
        elif largest < entry:
            largest = entry
    return ((smallest, "is the smallest number", largest,"is the largest number"))
print(minmax([3,5,7,-3,-5,-7]))
