def xoay_ma_tran(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return "Dữ liệu không hợp lệ: Không phải là ma trận NxN"

    n = len(matrix)

    # Chuyển vị ma trận
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Đảo ngược thứ tự của các hàng (hoặc cột)
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix

# Sử dụng ví dụ:
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ket_qua = xoay_ma_tran(ma_tran)
for hang in ket_qua:
    print(hang)
               