def factorial(n):
    # Trường hợp n âm, giai thừa không xác định, trả về -1
    if n < 0:
        return -1
    # Trường hợp n bằng 0, giai thừa là 1
    elif n == 0:
        return 1
    # Trường hợp n dương, tính giai thừa bằng cách gọi đệ quy
    else:
        return n * factorial(n - 1)

# Sử dụng ví dụ:
result = factorial(5)
print(result)
