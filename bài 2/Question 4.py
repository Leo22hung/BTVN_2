def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# Sử dụng ví dụ:
arrayA = [1, 3, 5]
arrayB = [2, 4, 6]

printUnorderedPairs(arrayA, arrayB)
