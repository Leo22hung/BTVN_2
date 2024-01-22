def powersOf2(n):
    # Trường hợp cơ bản: n < 1, trả về 0
    if n < 1:
        return 0
    # Trường hợp cơ bản: n == 1, in ra 1 và trả về 1
    elif n == 1:
        print(1)
        return 1
    # Trường hợp chung: tính lũy thừa của 2 bằng cách gọi đệ quy và nhân với 2
    else:
        prev = powersOf2(int(n / 2))
        curr = prev * 2
        print(curr)
        return curr

# Sử dụng ví dụ:
powersOf2(5)
