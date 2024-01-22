def so_ngay_tren_trung_binh(du_lieu_nhiet_do):
    nhiet_do_trung_binh = sum(du_lieu_nhiet_do) / len(du_lieu_nhiet_do)
    
    so_ngay_tren_trung_binh = sum(nhiet_do > nhiet_do_trung_binh for nhiet_do in du_lieu_nhiet_do)
    
    return so_ngay_tren_trung_binh

# Sử dụng ví dụ:
du_lieu_nhiet_do = [75, 80, 78, 82, 79, 85, 88, 90, 77, 76]
ket_qua = so_ngay_tren_trung_binh(du_lieu_nhiet_do)

print(f"Số ngày có nhiệt độ cao hơn trung bình: {ket_qua}")
