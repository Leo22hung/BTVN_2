def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(str(array[i]) + "," + str(array[j]))

# Sử dụng ví dụ:
my_array = [1, 2, 3]

printUnorderedPairs(my_array)
