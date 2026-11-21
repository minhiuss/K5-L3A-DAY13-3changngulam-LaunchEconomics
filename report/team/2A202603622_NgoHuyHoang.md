# Báo cáo cá nhân — NgoHuyHoang-2A202603622

## 1. Thông tin thành viên

- Họ tên: Ngô Huy Hoàng
- MSSV: 2A202603622
- Vai trong nhóm: Người kiểm số, phụ trách CP2

## 2. Phần việc phụ trách

Em phụ trách Nhiệm vụ B: chạy các kịch bản độ nhạy, so sánh giới hạn chạy lại và phân tích trường hợp phải xem lại 100%.

## 3. Đóng góp cụ thể

- Bổ sung `tinh_nhiem_vu_b()` và `in_nhiem_vu_b()` trong `src/lab13.py` để tính toàn bộ B1–B4 từ dữ liệu.
- Điền bảng B1 đủ 9 kịch bản và xếp hạng ba yếu tố ảnh hưởng lớn nhất.
- Tính B3 cho giới hạn 1, 2, 3 lần chạy và B4 với hai mức thời gian làm lại `9 phút` và `15,3 phút`.

## 4. Bằng chứng

- `src/lab13.py`: phần CP2.
- `report/team/bang_chi_phi.md`: các mục B1–B4.
- Kết quả chính: làm lại gấp đôi làm CPS tăng `51,8%`; giới hạn 2 lần cho tổng chi phí hệ thống thấp nhất `6.901.220 đ`; xem lại 100% cho CPS từ `11.743 đ` đến `12.415 đ` (simulated).

## 5. Công cụ AI đã dùng

Em dùng Codex để hỗ trợ đọc yêu cầu, triển khai code và rà soát báo cáo. Kết quả được kiểm tra bằng cách chạy `lab13.py`, đối chiếu với công thức trong tài liệu và chạy các assertion cho B1–B4.

## 6. Tự đánh giá

Phần CP2 đã đủ B1–B4, các số trong báo cáo được sinh từ code và các kết quả dùng dữ liệu giả lập đều có nhãn `simulated`.
