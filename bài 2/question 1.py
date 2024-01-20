def foo(array):
    total_sum = 0
    product = 1
    
    for i in array:
        total_sum += i
    
    for i in array:
        product *= i
    
    print("Sum = " + str(total_sum) + ", Product = " + str(product))

# Example usage:
my_array = [1, 2, 3, 4, 5]
foo(my_array)
