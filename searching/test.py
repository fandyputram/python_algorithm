arr = [1, 2, 3, 5, 1, 2, 3]

mapOccurence = {}

for i in range(len(arr)):
    key = arr[i]
    if key in mapOccurence:
        mapOccurence[key] += 1
    else:
        mapOccurence[key] = 1
    
print(mapOccurence)

# 1->2 2->2 3->2 5->1