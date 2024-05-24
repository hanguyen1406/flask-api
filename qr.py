import qrcode

# Dữ liệu muốn mã hóa thành mã QR
data = "'095094015600'||'HOÀNG MINH GIÁP'|'30/01/1994'|'Nam'|'30/01/2034'|'Phong Thạnh Tây B|Phước Long|Bạc Liêu'"

# Tạo mã QR
qr = qrcode.QRCode(
    version=7,  # phiên bản mã QR, giá trị từ 1 đến 40
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # mức độ sửa lỗi
    box_size=10,  # kích thước mỗi ô vuông trong mã QR
    border=4,  # kích thước viền (ô vuông)
)

qr.add_data(data)
qr.make(fit=True)

# Tạo ảnh cho mã QR
img = qr.make_image(fill_color="black", back_color="white")

# Lưu ảnh mã QR
img.save("qrcode.png")