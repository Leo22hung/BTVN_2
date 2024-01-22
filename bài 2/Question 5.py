def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# Sử dụng ví dụ:
arrayA = [1, 3, 5]
arrayB = [2, 4, 6]

printUnorderedPairs(arrayA, arrayB)
