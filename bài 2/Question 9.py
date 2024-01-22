def allFib(n):
    # Duyệt qua các số Fibonacci từ 0 đến n-1
    for i in range(n):
        print(str(i) + ": " + str(fib(i)))

def fib(n):
    # Trường hợp cơ bản: n <= 0, trả về 0
    if n <= 0:
        return 0
    # Trường hợp cơ bản: n == 1, trả về 1
    elif n == 1:
        return 1
    # Trường hợp chung: tính số Fibonacci bằng cách gọi đệ quy
    else:
        return fib(n - 1) + fib(n - 2)

# Sử dụng ví dụ:
allFib(5)
