def tim_cac_cap_co_tong(arr, tong_muc_tieu):
    cac_cap = []
    cac_so_da_gap = set()

    for num in arr:
        so_bu = tong_muc_tieu - num

        if so_bu in cac_so_da_gap:
            cac_cap.append((num, so_bu))

        cac_so_da_gap.add(num)

    return cac_cap

# Ví dụ sử dụng:
so_nguyen = [1, 2, 3, 4, 5, 6, 7]
tong_muc_tieu = 8

ket_qua_cac_cap = tim_cac_cap_co_tong(so_nguyen, tong_muc_tieu)

if ket_qua_cac_cap:
    print(f"Các cặp có tổng {tong_muc_tieu}: {ket_qua_cac_cap}")
else:
    print(f"Không có cặp số nào có tổng bằng {tong_muc_tieu}")
