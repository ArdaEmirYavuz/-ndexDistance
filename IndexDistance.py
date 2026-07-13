numbers = [1,3,1,1,2]
def DistanceSummary(numbers):
    indexList = []
    indexOut = -1
    for i in numbers:
        total = 0
        indexİn = 0
        indexOut +=1
        for j in numbers:
            if(numbers[indexİn] == numbers[indexOut]):
                total += abs(indexOut - indexİn)
                indexİn +=1
                continue
            else:
                indexİn +=1
                continue
        indexList.append(total)
    return indexList
conclusion = DistanceSummary(numbers)
print(conclusion)
